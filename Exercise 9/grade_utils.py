# grade_utils.py
#This code is written by gemini

def calculate_percentage(score: int, total: int) -> float:
    """Compute the percentage score, preventing division by zero."""
    if total <= 0:
        return 0.0
    return (score / total) * 100


def get_grade_report(percentage: float) -> tuple[str, str]:
    """Determine the letter grade and motivation message based on percentage score."""
    if percentage >= 90:
        return "A", "Outstanding! You really know your Python!"
    if percentage >= 75:
        return "B", "Great job! Solid Python knowledge."
    if percentage >= 60:
        return "C", "Good effort. Keep practising!"
    if percentage >= 40:
        return "D", "Keep studying -- you're getting there."
    return "F", "Review the lessons and try again!"
