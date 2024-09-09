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

st.sidebar.subheader("🔑 Enter OpenAI API Key")
with st.sidebar:
    openai_key = st.sidebar.text_input("API Key", type="password", placeholder="Enter API key")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    
st.title("🔍 Chat with Search")
st.write("Enter a query to search for information:")

# Chat with Search logic
search_query = st.text_input("Search for information...", key="search_input")
if search_query:
    st.write(f"**You searched for**: {search_query}")
    # Add your search-related chat logic here
    st.write("Searching for the information... 🔍")
