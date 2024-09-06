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

st.sidebar.subheader("🔑 Optional: Enter OpenAI API Key")
openai_key = st.sidebar.text_input("API Key", type="password", placeholder="Enter API key")

st.title("📄 Q/A with PDF")
st.write("Upload a PDF document to ask questions from it:")

# Q/A with PDF logic
uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"], key="pdf_uploader")
if uploaded_pdf:
    st.write("PDF uploaded successfully! You can now ask questions related to the document.")
    question = st.text_input("Ask a question related to the PDF...", key="pdf_question")
    if question:
        st.write(f"**Your question**: {question}")
        # Add your PDF Q/A logic here
        st.write("Processing PDF for relevant answers... 📄")
