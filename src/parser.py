"""
parser.py
----------
Responsible for extracting raw text from PDF and DOCX resumes.
"""
from xml.dom.minidom import Document

import pdfplumber
import docx
import os


def extract_text(file_path: object):
    """
    Detects file type and extracts text accordingly.

    Parameters:
        file_path (str): Path to the resume file

    Returns:
        str: Extracted resume text
    """

    # Get file extension (pdf or docx)
    _, ext = os.path.splitext(file_path)

    # Handle PDF files
    if ext.lower() == ".pdf":
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text

    # Handle DOCX files
    elif ext.lower() == ".docx":
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        raise ValueError("Unsupported file format")
