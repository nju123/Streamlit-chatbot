import streamlit as st


# initialize the chatopenai object
chat = None
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""

st.set_page_config(page_title="OpenAI Settings", layout="wide")

st.title("OpenAI Setting")

openai_api_key = st.text_input("API Key",value=st.session_state["OPENAI_API_KEY"],key=None,type="password")

saved = st.button("Submit")

if saved is True:
    st.session_state["OPENAI_API_KEY"] = openai_api_key