from flask import Blueprint, jsonify, request
from utils.genai_utils import generate_answer_with_genai

comment_only_bp = Blueprint("comment_only", __name__)

# Gemini case comment prompt structure
STRUCTURE_PROMPT = (
    "You are Luciano Horta, a DocuSign Technical Support Engineer II - eSign. Based on the text below, generate a professional case comment "
    "in first person, for example: 'I reviewed...', 'I have sent...', 'I created...'. Output in HTML format using this structure:\n\n"
    "<h3 style='color:red;'>Case Comment:</h3>\n"
    "<p><strong>[Matter]:</strong> Briefly explain the client's issue.</p>\n"
    "<p><strong>[Action]:</strong> Describe what you investigated or did.</p>\n"
    "<p><strong>[Next Steps]:</strong> State what is expected or what will be done next.</p>\n"
    "<p><strong>[Links]:</strong> Add relevant links, or say 'N/A'.</p>\n\n"
    "Do not include anything outside this format. Here is the case text:\n\n"
)


@comment_only_bp.route("/comment-only", methods=["POST"])
def generate_case_comment():
    try:
        data = request.get_json()
        text = data.get("text", "").strip()

        if not text:
            return jsonify({"error": "Missing 'text' field in request body."}), 400

        # Prepare full prompt
        prompt = STRUCTURE_PROMPT + text

        # Get response from Gemini
        raw_comment = generate_answer_with_genai(prompt)

        # Clean output (remove code block wrappers, just in case)
        cleaned_comment = raw_comment.replace("```html", "").replace("```", "").strip()

        return jsonify({"comment": cleaned_comment})

    except Exception as e:
        print(f"[ERROR] Failed to generate comment: {e}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
