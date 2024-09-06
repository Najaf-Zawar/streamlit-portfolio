import streamlit as st
from streamlit_extras.switch_page_button import switch_page  # Use this to switch pages

# Page Navigation in Sidebar
st.sidebar.title("📚 OpenAI Assistant")
st.sidebar.subheader("Features")

# Add navigation buttons to switch between pages
if st.sidebar.button("🤖 Chatbot"):
    switch_page("openai_chatbot")

if st.sidebar.button("📄 Q/A with PDF"):
    switch_page("openai_qa")

if st.sidebar.button("🔍 Chat with Search"):
    switch_page("openai_search")


