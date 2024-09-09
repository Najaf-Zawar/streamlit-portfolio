import streamlit as st
import openai
# import anthropic

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
    anthropic_api_key = st.text_input("OpenAI API Key", key="file_qa_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

st.title("📄 Q/A with PDF")
st.write("Upload a PDF document to ask questions from it:")

# Q/A with PDF logic
uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))

question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file and question and not anthropic_api_key:
    st.info("Please add your Anthropic API key to continue.")

# if uploaded_file and question and anthropic_api_key:
#     article = uploaded_file.read().decode()
#     prompt = f"""{anthropic.HUMAN_PROMPT} Here's an article:\n\n
#     {article}\n\n\n\n{question}{anthropic.AI_PROMPT}"""

#     client = anthropic.Client(api_key=anthropic_api_key)
#     response = client.completions.create(
#         prompt=prompt,
#         stop_sequences=[anthropic.HUMAN_PROMPT],
#         model="claude-v1", #"claude-2" for Claude 2 model
#         max_tokens_to_sample=100,
#     )
#     st.write("### Answer")
#     st.write(response.completion)