"""
skills_extractor.py
-------------------
Extracts and categorizes skills using NLP + keyword matching.
"""

import spacy

nlp = spacy.load("en_core_web_sm")

TECHNICAL_SKILLS = ["python", "sql", "machine learning", "pandas", "numpy"]
TOOLS = ["git", "docker", "aws", "excel"]
SOFT_SKILLS = ["communication", "teamwork", "problem solving"]


def extract_skills(text):
    """
    Extracts skills from resume text.

    Parameters:
        text (str): Resume text

    Returns:
        dict: Categorised skills
    """

    doc = nlp(text.lower())

    found_skills = {
        "technical": [],
        "tools": [],
        "soft": []
    }

    for token in doc:
        if token.text in TECHNICAL_SKILLS:
            found_skills["technical"].append(token.text)
        elif token.text in TOOLS:
            found_skills["tools"].append(token.text)
        elif token.text in SOFT_SKILLS:
            found_skills["soft"].append(token.text)

    return found_skills
