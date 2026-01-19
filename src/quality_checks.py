"""
quality_checks.py
-----------------
Performs rule-based quality checks on resume content.
"""

import re


ACTION_VERBS = [
    "developed", "built", "designed", "implemented",
    "analysed", "led", "created", "improved"
]


def analyse_quality(sections):
    """
    Runs quality checks across resume sections.

    Parameters:
        sections (dict): Parsed resume sections

    Returns:
        list: List of detected issues
    """

    issues = []

    # Check for missing key sections
    required_sections = ["summary", "skills", "experience", "education"]
    for sec in required_sections:
        if sec not in sections or len(sections[sec]) < 50:
            issues.append(f"Missing or weak {sec.title()} section")

    # Check resume length
    total_length = sum(len(s) for s in sections.values())
    if total_length < 1500:
        issues.append("Resume may be too short")
    elif total_length > 6000:
        issues.append("Resume may be too long")

    # Bullet point usage
    if "-" not in sections.get("experience", ""):
        issues.append("Experience section lacks bullet points")

    # Action verb usage
    verbs_found = sum(
        1 for verb in ACTION_VERBS
        if verb in sections.get("experience", "").lower()
    )
    if verbs_found < 3:
        issues.append("Experience section lacks strong action verbs")

    return issues
