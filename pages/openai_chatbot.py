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

st.title("🤖 Chatbot")
st.write("Welcome to the chatbot! Type your queries below:")

# Chatbot logic
user_input = st.text_input("Ask me anything...", key="chatbot_input")
if user_input:
    st.write(f"**You asked**: {user_input}")
    # Add your chatbot response logic here
    st.write("Chatbot is generating a response... 🤖")
