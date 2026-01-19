"""
feedback_generator.py
---------------------
Generates structured feedback based on detected issues.
"""

def generate_feedback(issues, skills):
    """
    Converts issues into actionable feedback.

    Parameters:
        issues (list): Detected quality issues
        skills (dict): Extracted skills

    Returns:
        list: Feedback messages
    """

    feedback = []

    for issue in issues:
        if "action verbs" in issue:
            feedback.append("Use strong action verbs to start experience bullet points.")
        elif "too short" in issue:
            feedback.append("Expand experience with measurable impact and results.")
        else:
            feedback.append(issue)

    if not skills["technical"]:
        feedback.append("Missing technical skills commonly expected in data roles.")

    return feedback
