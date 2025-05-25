from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

import os
import shutil
import fitz

upload_bp = Blueprint("upload", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@upload_bp.route("/upload", methods=["POST"])
def upload_pdf():
    clear = request.args.get("clear", "false").lower() == "true"
    source = request.args.get("source", "docusign")
    doc_type = request.args.get("doc_type", "how-to")  

    if clear:
        shutil.rmtree("chroma_db")
        os.makedirs("chroma_db", exist_ok=True)

    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Extract and chunk text
    extracted_text = extract_text_from_pdf(filepath)
    chunks = break_text(extracted_text, piece_length=600, overlay=100)

    # Save with metadata
    #save_chunks_with_metadata(chunks, filename=filename, source=source, doc_type=doc_type)

    return jsonify({"message": "File processed successfully", "filename": filename})


def extract_text_from_pdf(filepath):
    """Extracts text from a PDF file."""
    doc = fitz.open(filepath)
    text = "\n".join([page.get_text("text") for page in doc])
    return text.strip()


def break_text(text, piece_length=1000, overlay=200):
    """Splits text into overlapping chunks."""
    if piece_length <= overlay:
        raise ValueError("Piece length must be greater than overlay.")
    
    pieces = []
    start = 0
    while start < len(text):
        end = start + piece_length
        piece = text[start:end]
        pieces.append(piece)
        start += piece_length - overlay  # Move start with overlap
    
    return pieces
