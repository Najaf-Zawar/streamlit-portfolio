import streamlit as st
from openai import OpenAI
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
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

st.title("🤖 Chatbot")
st.write("Welcome to the chatbot! Type your queries below:")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)