"""
section_detector.py
-------------------
Identifies major resume sections using keyword matching.
"""

import re


SECTION_HEADERS = {
    "summary": ["summary", "profile", "about me"],
    "skills": ["skills", "technical skills"],
    "experience": ["experience", "work history", "employment"],
    "education": ["education", "qualifications"]
}


def detect_sections(text):
    """
    Splits resume text into logical sections.

    Parameters:
        text (str): Raw resume text

    Returns:
        dict: Section name -> section content
    """

    sections = {}
    lines = text.split("\n")
    current_section = "other"
    sections[current_section] = []

    for line in lines:
        lower_line = line.lower()

        # Check if line matches a section header
        for section, keywords in SECTION_HEADERS.items():
            if any(re.search(rf"\b{k}\b", lower_line) for k in keywords):
                current_section = section
                sections[current_section] = []
                break

        sections[current_section].append(line)

    # Join lists into text blocks
    return {k: "\n".join(v).strip() for k, v in sections.items()}
