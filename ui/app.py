import streamlit as st
from generation.generate_local import generate_answer

st.set_page_config(page_title="DL Chatbot", page_icon="🤖")

st.title("🤖 Deep Learning Chatbot (RAG)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask about Deep Learning...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = generate_answer(user_input)
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})