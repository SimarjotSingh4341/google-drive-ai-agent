import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "google-drive-ai-agent-production.up.railway.app")

st.set_page_config(page_title="Google Drive AI Assistant")

st.title("Google Drive AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Search files in Google Drive...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    response = requests.post(
        BACKEND_URL,
        json={"message": prompt}
    )

    answer = response.json()["response"]

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.markdown(answer)
