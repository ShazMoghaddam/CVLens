"""
main.py
-------
Application entry point for CVLens.
"""

from parser import extract_text
from section_detector import detect_sections
from quality_checks import analyse_quality
from skills_extractor import extract_skills
from feedback_generator import generate_feedback


def run_cvlens(file_path):
    """
    Runs the full CVLens pipeline.

    Parameters:
        file_path (str): Resume file path
    """

    text = extract_text(file_path)
    sections = detect_sections(text)
    issues = analyse_quality(sections)
    skills = extract_skills(text)
    feedback = generate_feedback(issues, skills)

    print("\n--- CVLens Feedback ---\n")
    for item in feedback:
        print(f"- {item}")


if __name__ == "__main__":
    run_cvlens("data/sample_resume.pdf")
