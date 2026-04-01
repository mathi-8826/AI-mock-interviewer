"""
AI-Powered Mock Interviewer – Data Scientist Role
Built with CrewAI + Streamlit
"""

import os
import streamlit as st
from dotenv import load_dotenv
from tasks import INTERVIEW_QUESTIONS
from crew import get_feedback

load_dotenv()

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Mock Interviewer – Data Scientist",
    page_icon="🤖",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Session-state initialisation
# ---------------------------------------------------------------------------
if "question_index" not in st.session_state:
    st.session_state.question_index = 0          # current question pointer
if "answers" not in st.session_state:
    st.session_state.answers = []                # list of (question, answer, feedback)
if "feedback_pending" not in st.session_state:
    st.session_state.feedback_pending = False    # waiting to show feedback?
if "current_feedback" not in st.session_state:
    st.session_state.current_feedback = ""
if "interview_done" not in st.session_state:
    st.session_state.interview_done = False

TOTAL_QUESTIONS = len(INTERVIEW_QUESTIONS)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("🤖 AI Mock Interviewer")
st.subheader("Role: **Data Scientist**")
st.markdown("---")

# ---------------------------------------------------------------------------
# Gemini API key check
# ---------------------------------------------------------------------------
api_key = os.getenv("GEMINI_API_KEY", "")
if not api_key:
    api_key = st.text_input(
        "🔑 Enter your Gemini API Key to begin",
        type="password",
        placeholder="AIza...",
    )
    if api_key:
        os.environ["GEMINI_API_KEY"] = api_key
        os.environ["GOOGLE_API_KEY"] = api_key  # langchain-google-genai reads this
    else:
        st.info("Please enter your Gemini API key above to start the interview.")
        st.stop()
else:
    os.environ["GOOGLE_API_KEY"] = api_key

# ---------------------------------------------------------------------------
# Interview complete screen
# ---------------------------------------------------------------------------
if st.session_state.interview_done:
    st.success("🎉 Interview Complete! Here's your full session summary:")
    st.markdown("---")
    for i, (q, a, fb) in enumerate(st.session_state.answers, 1):
        with st.expander(f"Question {i}: {q}", expanded=False):
            st.markdown(f"**Your Answer:**\n\n{a}")
            st.markdown("---")
            _icon = "✅" if any(
                word in fb.lower()
                for word in ["good", "correct", "great", "excellent", "well", "strong"]
            ) else "💡"
            st.markdown(f"{_icon} **Feedback:** {fb}")

    st.markdown("---")
    if st.button("🔄 Restart Interview"):
        for key in ["question_index", "answers", "feedback_pending",
                    "current_feedback", "interview_done"]:
            del st.session_state[key]
        st.rerun()
    st.stop()

# ---------------------------------------------------------------------------
# Progress bar
# ---------------------------------------------------------------------------
idx = st.session_state.question_index
progress = idx / TOTAL_QUESTIONS
st.progress(progress, text=f"Question {idx + 1} of {TOTAL_QUESTIONS}")

# ---------------------------------------------------------------------------
# Current question
# ---------------------------------------------------------------------------
current_question = INTERVIEW_QUESTIONS[idx]

st.markdown(f"### ❓ Question {idx + 1}")
st.info(current_question)

# ---------------------------------------------------------------------------
# Feedback display (shown after submission, before moving on)
# ---------------------------------------------------------------------------
if st.session_state.feedback_pending:
    fb = st.session_state.current_feedback
    positive_keywords = ["good", "correct", "great", "excellent", "well", "strong", "accurate"]
    if any(word in fb.lower() for word in positive_keywords):
        st.success(f"✅ **Feedback:** {fb}")
    else:
        st.warning(f"💡 **Feedback:** {fb}")

    if st.button("➡️ Next Question" if idx < TOTAL_QUESTIONS - 1 else "🏁 Finish Interview"):
        st.session_state.feedback_pending = False
        st.session_state.current_feedback = ""
        if idx + 1 < TOTAL_QUESTIONS:
            st.session_state.question_index += 1
        else:
            st.session_state.interview_done = True
        st.rerun()

# ---------------------------------------------------------------------------
# Answer input (hidden while feedback is visible)
# ---------------------------------------------------------------------------
else:
    with st.form(key=f"answer_form_{idx}"):
        user_answer = st.text_area(
            "✍️ Your Answer",
            height=160,
            placeholder="Type your answer here...",
        )
        submitted = st.form_submit_button("📨 Submit Answer")

    if submitted:
        if not user_answer.strip():
            st.error("Please type an answer before submitting.")
        else:
            with st.spinner("🤔 Evaluating your answer..."):
                try:
                    feedback = get_feedback(current_question, user_answer)
                except Exception as e:
                    feedback = f"Could not generate AI feedback: {e}"

            st.session_state.answers.append(
                (current_question, user_answer, feedback)
            )
            st.session_state.current_feedback = feedback
            st.session_state.feedback_pending = True
            st.rerun()

# ---------------------------------------------------------------------------
# Sidebar – tips
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 📋 Interview Tips")
    st.markdown(
        """
- Take your time before answering.
- Use the **STAR** method for behavioural questions.
- Back claims with **examples** from experience.
- It's okay to think out loud!
        """
    )
    st.markdown("---")
    st.markdown("**Role:** Data Scientist")
    st.markdown(f"**Questions:** {TOTAL_QUESTIONS}")
    st.markdown(f"**Answered:** {len(st.session_state.answers)}")
