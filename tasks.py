from crewai import Task
from agents import create_feedback_agent


# ---------------------------------------------------------------------------
# The 6 role-specific interview questions for a Data Scientist position
# ---------------------------------------------------------------------------
INTERVIEW_QUESTIONS = [
    "What is overfitting in machine learning, and how can you prevent it?",
    "Explain the difference between supervised and unsupervised learning with examples.",
    "What is cross-validation, and why is it important when evaluating a model?",
    "Explain the bias-variance trade-off and how it affects model performance.",
    "What is the difference between regression and classification? Give a real-world example of each.",
    "How would you handle missing data in a dataset before training a machine learning model?",
]


def create_feedback_task(question: str, answer: str) -> Task:
    """Creates a CrewAI Task that evaluates a candidate's answer."""
    feedback_agent = create_feedback_agent()

    return Task(
        description=(
            f"Interview Question: {question}\n\n"
            f"Candidate's Answer: {answer}\n\n"
            "Evaluate the candidate's answer. In 2–3 sentences:\n"
            "1. Acknowledge what they got right.\n"
            "2. Point out any missing details or misconceptions.\n"
            "3. Optionally suggest what a stronger answer would include.\n"
            "Keep the tone encouraging and professional."
        ),
        expected_output=(
            "A short 2–3 sentence feedback comment on the candidate's answer."
        ),
        agent=feedback_agent,
    )
