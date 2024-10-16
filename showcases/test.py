import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.
from models.openai import Generator
import streamlit as st

def test():
    state = st.session_state
    # col1, col2 = st.columns([1, 1])
    with st.sidebar:
        st.subheader("LangGPT構造化プロンプト")
        prompt = st.text_area("langgpt_prompt",state.prompt,height=500,label_visibility="collapsed")
        if st.button("プロンプトを保存"):
            if "test_messages" not in state:
                state.test_messages = []
                pass
            # state.test_messages = [{"role": "system", "content": prompt}]
            state.prompt = prompt
            st.rerun()
            pass
        pass
    ## メッセージを表示するチャットボット
    if "test_messages" not in state:
        state.test_messages = [{"role": "system", "content": state.prompt}]
        response = state.generator.generate_response(state.test_messages)
        state.test_messages.append({"role": "assistant", "content": response})
        st.rerun()
        pass
    # st.subheader("LangGPT会話")
    for message in state.test_messages:
        if message["role"] == "system":
            continue
        st.chat_message(message["role"]).write(message["content"])
        pass
    
    if prompt := st.chat_input("会話を入力"):
        state.test_messages.append({"role": "user", "content": prompt})
        response = state.generator.generate_response(state.test_messages)
        state.test_messages.append({"role": "assistant", "content": response})
        st.rerun()
        pass
    pass
