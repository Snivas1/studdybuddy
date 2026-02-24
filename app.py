import streamlit as st
from components.explainer import show_explainer
from components.summarizer import show_summarizer
from components.quiz_generator import show_quiz
from components.flashcards import show_flashcards

st.set_page_config(page_title="AI Study Buddy", layout="wide")

st.title("🎓 AI-Powered Study Buddy")

menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Concept Explainer", "Notes Summarizer", "Quiz Generator", "Flashcards"]
)

if menu == "Concept Explainer":
    show_explainer()

elif menu == "Notes Summarizer":
    show_summarizer()

elif menu == "Quiz Generator":
    show_quiz()

elif menu == "Flashcards":
    show_flashcards()