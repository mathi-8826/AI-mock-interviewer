import os
import google.generativeai as genai


def get_feedback(question: str, answer: str) -> str:
    """
    Calls the Gemini API directly to generate feedback for the given
    question/answer pair. Returns the feedback string.
    """
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = (
        f"Interview Question: {question}\n\n"
        f"Candidate's Answer: {answer}\n\n"
        "Evaluate the candidate's answer in 2-3 sentences:\n"
        "1. Acknowledge what they got right.\n"
        "2. Point out any missing details or misconceptions.\n"
        "3. Optionally suggest what a stronger answer would include.\n"
        "Keep the tone encouraging and professional."
    )

    response = model.generate_content(prompt)
    return response.text.strip()
