import google.generativeai as genai
from flask import Blueprint, jsonify, request
import os
from dotenv import load_dotenv
import re
#from utils.query import query_chromadb  

from utils.generate_questions import generate_questions_from_subject_and_description
from utils.chroma_query import query_chromadb_questions  
# Load environment variables from .env file
load_dotenv()

summary_bp = Blueprint("summary", __name__)

# Get API Key from environment
GENAI_API_KEY = os.getenv("GOOGLE_GENERATIVE_AI_API_KEY")

if not GENAI_API_KEY:
    raise ValueError("API key is missing! Check your .env file.")


# System instructions for AI
system_message = (
    "You are an AI assistant working as a support agent for DocuSign. "
    "You directly assist customers with their cases and should never tell them to contact DocuSign support. "
    "Instead, provide clear guidance as if you are the support agent handling the case. "
    "Use the provided knowledge base references where applicable to ensure responses are relevant."
)


# Example Case to Guide AI
example_case = (
    "Example Case:\n"
    "Case Number: 15036075\n"
    "Subject: Please see changes in FIFA FW settings below and inform about required changes in environment\n"
    "Description: FIFA is updating their firewall and public IP. They request confirmation on whether any actions are needed on our side to ensure a smooth transition. "
    "They emphasize that DNS names remain unchanged, and they provide a deadline for adjustments. "
    "They also provide old and new IP addresses and ask for confirmation on any necessary firewall rule changes before March 28 at 18:00 CET.\n"
    "Key Takeaway: The user needs to verify whether any changes are required on their side and update firewall rules before the deadline."
)

# Expected Response Model in HTML
response_model = (
    "Example of a case overview and comment in HTML format:\n\n"
    "<h2>Case Overview:</h2>"
    "<h3>Case Number: 12345678</h3>"
    "<h3><strong>Subject:</strong></h3><p>User Receiving Error Message When Logging On via SSO</p>"
    "<h3><strong>Description:</strong></h3><p>The user (victor.casado.mejia@avanade.com) is unable to log in via Single Sign-On (SSO) and is receiving the error message: "
    '"The federated identifier for single sign-on does not match the values enabled for this user. Contact your DocuSign administrator."</p>'

    "<h3><strong>Possible Causes:</strong></h3>"
    "<ul>"
    "<li>The federated identifier (NameID or email address) in the Identity Provider (IdP) has changed and does not match what is stored in DocuSign.</li>"
    "<li>The federated identifier in DocuSign may have been reset, causing a mismatch with the IdP.</li>"
    "</ul>"

    "<h3><strong>Recommended Next Steps:</strong></h3>"
    "<ul>"
    "<li><strong>Confirm with the IT team</strong> if the user’s NameID/email in the IdP has changed. If possible, revert it to the original value.</li>"
    "<li><strong>Reset the federated identifier in DocuSign</strong> if reverting in the IdP is not possible. A DocuSign administrator can do this by: "
    "<ul>"
    "<li>Logging into DocuSign Admin.</li>"
    "<li>Navigating to the Users tile.</li>"
    "<li>Locating the affected user.</li>"
    "<li>Going to the Security tab and clicking 'Clear' to reset the Federated Identifier.</li>"
    "<li>The user should then attempt to log in again via SSO.</li>"
    "</ul></li>"
    "<li>Ensure that the NameID or email sent in the SAML assertion from the IdP exactly matches the user's primary email in DocuSign.</li>"
    "<li><strong>Escalate if necessary</strong>: If further assistance is needed, consider escalating the case or offering to schedule a meeting with the IT team for troubleshooting.</li>"
    "</ul>"
)



# Email Response Example
email_response_example = (
    "<h3 style='color:red;'>Response Email:</h3>"
    "<p><strong>Subject:</strong> Assistance with DEMO Mode Account Switching</p>"
    "<p>Dear [Client's Name],</p>"
    "<p>Thank you for reaching out regarding the issue where a user in DEMO MODE is unable to switch accounts.</p>"
    "<p>To assist you effectively, please check the following:</p>"

    "<ol>"
    "<li><strong>Verify User Access:</strong>"
    "<ul>"
    "<li>Ensure the user has multiple accounts linked to their email.</li>"
    "<li>Check if their role allows account switching.</li>"
    "</ul></li>"
    
    "<li><strong>Admin Settings Check:</strong>"
    "<ul>"
    "<li>If the user should have access to multiple accounts, confirm that the option to switch accounts is enabled in Admin Settings.</li>"
    "</ul></li>"
    
    "<li><strong>Try Logging Out and Back In:</strong>"
    "<ul>"
    "<li>Ask the user to log out of DocuSign and log back in to see if the option appears.</li>"
    "</ul></li>"
    
    "<li><strong>Further Assistance:</strong>"
    "<ul>"
    "<li>If the issue persists, we recommend escalating this to our support team. Please provide the affected user’s email address and account details, and we will investigate further.</li>"
    "</ul></li>"
    "</ol>"

    "<p>Let us know if you need any additional guidance. We’re happy to help!</p>"

    "<p>Best regards,</p>"
    "<p>[Your Name]</p>"
    "<p>[Your Position]</p>"
    "<p>DocuSign Support Team</p>"
)

overview_model_example = (
    "<h2>Case Overview:</h2>\n\n"
    "<h3>Case Number: 14711497</h3>"
    
    "<h3><strong>Subject:</strong></h3>"
    "<p>Uploading Contract Issues</p>"
    
    "<h3><strong>Description:</strong></h3>"
    "<p>The client is experiencing an issue when uploading a contract from Google Drive using a DocuSign integration. "
    "Instead of selecting the correct folder (<strong>\"Tenancy Contract Folder\"</strong>), the system uploads the "
    "first file or folder in the structure. The user attempted to reorder folders to prioritize the correct one, "
    "but the issue persisted.</p>"
    
    "<h3><strong>Customer Request:</strong></h3>"
    "<p>The client wants to ensure that the correct folder ('Tenancy Contract Folder') is selected during the upload process.</p>"
    
    "<h3><strong>Support Actions:</strong></h3>"
    "<ul>"
    "<li>Requested a HAR file to analyze the upload issue.</li>"
    "<li>Received the HAR file and confirmed download.</li>"
    "<li>Escalated the issue to the engineering team for investigation.</li>"
    "</ul>"
    
    "<h3><strong>Current Status:</strong></h3>"
    "<p>Waiting for feedback from engineering after initial analysis of the HAR file.</p>"
)



# Function to structure ChromaDB results
def format_chroma_results(chroma_results):
    """Formats ChromaDB results into a structured string for the AI prompt."""
    if not chroma_results or not chroma_results.get("documents"):
        return "No relevant references found in ChromaDB."

    formatted_results = []
    for doc in chroma_results["documents"][0]:
        snippet = doc[:500]  # Limit snippet size
        formatted_results.append(f"- {snippet} [...]")

    return "\n".join(formatted_results)

@summary_bp.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        text = data.get("text", "")

        print(f"Received text for summarization: {text}")


        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Extract Subject and Description using Regex
        subject_match = re.search(r"(?i)Subject:\s*(.*)", text)
        description_match = re.search(r"(?i)Description:\s*(.*)", text)
        #extra_match = re.search(r"(?i)^\s*Extra(?: information)?:\s*((?:.|\n)*?)(?:\n\s*\n|$)", text, re.MULTILINE)
        extra_match = re.search(r"(?i)^\s*Extra(?: information)?:\s*(.*)", text, re.MULTILINE | re.DOTALL)



        subject = subject_match.group(1).strip() if subject_match else "No Subject Found"
        description = description_match.group(1).strip() if description_match else "No Description Found"
        extra = extra_match.group(1).strip() if extra_match else None

        print(f"extra information ---------------------------: {extra}")
        
        

        #chroma_results = query_chromadb(subject, description)
        #print(f"ChromaDB Results >>>>>>>>>>>>>>> : {chroma_results}")

        #chroma_context = "\n".join([f"- {result}" for result in chroma_results])
        questions = generate_questions_from_subject_and_description(subject, description)
        chroma_results = query_chromadb_questions(questions)

        # chroma_context = "\n".join(formatted_snippets)

        formatted_snippets = []
        how_to_references = []

        for result in chroma_results:
            for doc, metadata in zip(result.get("documents", []), result.get("metadatas", [])):
                snippet = doc[:500]
                doc_type = metadata.get("type", "").lower()
                source = metadata.get("source", "unknown")
                formatted = f"- ({doc_type.upper()} from {source}) {snippet} [...]"

                if doc_type == "kb":
                    how_to_references.append(formatted)
                else:
                    formatted_snippets.append(formatted)

        chroma_context = "\n".join(formatted_snippets)
        kb_reference_block = "\n".join(how_to_references)

        full_prompt = (
            f"Separate each section with a line break. Use HTML.\n\n"
            f"{system_message}\n\n{example_case}\n\n{response_model}\n\n"
            f"Now summarize the following text in the same format:\n{overview_model_example}\n\n\n\n"
            f"Here are some relevant references:\n{chroma_context}\n\n"
            f"Use this extra information to build the answer. this is the agent finds, image text captured, envelope history, slack lconversation, etc{extra}\n\n"
            f"Use the provided references where applicable when crafting the response.\n\n"
            f"If any references are from Knowledge Base (KB), include a section titled <b>Helpful How-To References (from KB)</b> at the end of the response, summarizing their content.\n\n"
            f"Now create a #response email - if the last email on the case is mine (Luciano) you don't need to create it, if the email is from the user or if there is no response you need to create one:\n{email_response_example}\n\n"
            f"{text}\n\n"
            f"<b>How-To References:</b>\n{kb_reference_block}\n\n"
            f"After the response, provide the database finds text only:\n{chroma_results}\n\n"
        )


        try:
            # Authenticate (only once, globally — best put this at the top of your module)
            genai.configure(api_key=GENAI_API_KEY)

            # Create the model instance
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")

            # Generate content
            response = model.generate_content(full_prompt)

            #print(f"AI Response -----------------------------------------------------------------------------       : {response}")

            if response and response.candidates:
                summary = response.candidates[0].content.parts[0].text
            else:
                summary = "No summary generated."

            clean_summary = summary.replace("```html", "").replace("```", "")

            return jsonify({
                "summary": clean_summary,
                "chroma_results": chroma_results
            })

        except Exception as ai_error:
            print(f"Summarization failed: {ai_error}")
            return jsonify({
                "error": "AI summarization failed, but ChromaDB results are available.",
                "chroma_results": chroma_results
            }), 200

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return jsonify({"error": str(e)}), 500