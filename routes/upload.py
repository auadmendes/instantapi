from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

import os
import shutil

from utils.doc_utils import extract_text_from_file
from utils.text_utils import break_text
from utils.chroma_utils import save_to_chroma


upload_bp = Blueprint("upload", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    clear = request.args.get("clear", "false").lower() == "true"
    source = request.args.get("source", "docusign")

    doc_type = request.args.get("doc_type", "how-to")
    print("Received doc_type:", doc_type)


    if clear:
        shutil.rmtree("chroma_db", ignore_errors=True)
        os.makedirs("chroma_db", exist_ok=True)

    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        text = extract_text_from_file(filepath)
    except Exception as e:
        return jsonify({"error": f"Extraction failed: {str(e)}"}), 500

    if not text.strip():
        return jsonify({"error": "No text extracted from file"}), 400

    chunks = break_text(text, piece_length=600, overlay=100)

    # 👇 Simulate saving to ChromaDB by printing
    metadata = {
        "filename": filename,
        "source": source,
        "doc_type": doc_type,
    }
    save_to_chroma(chunks, metadata)

    return jsonify({
        "message": "File processed successfully",
        "filename": filename,
        "doc_type": doc_type,
        "chunk_count": len(chunks),
        "sample_chunk": chunks[0] if chunks else "No chunks created"
    })
