import os
from docx import Document
import fitz  # PyMuPDF

def extract_text_from_file(filepath: str) -> str:
    """
    Detect file extension and extract text accordingly.
    """
    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(filepath)
    elif ext == ".docx":
        return extract_text_from_docx(filepath)
    elif ext == ".md":
        return extract_text_from_md(filepath)
    elif ext == ".doc":
        raise ValueError("⚠️ .doc format not supported. Please upload .docx instead.")
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def extract_text_from_pdf(filepath: str) -> str:
    """
    Extracts text from a PDF file using PyMuPDF (fitz).
    """
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()


def extract_text_from_docx(filepath: str) -> str:
    """
    Extracts text from a .docx file.
    """
    doc = Document(filepath)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])


def extract_text_from_md(filepath: str) -> str:
    """
    Extracts raw text from a Markdown (.md) file.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read().strip()
