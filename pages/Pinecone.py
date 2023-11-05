import streamlit as st

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ""

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ""

st.title("Pinecone Setting")

pinecone_api_key = st.text_input("API Key",value=st.session_state["PINECONE_API_KEY"],key=None,type="default")
environment = st.text_input("Environment",value=st.session_state["PINECONE_ENVIRONMENT"],key=None,type="default")

saved = st.button("Submit")

if saved is True:
    st.session_state["PINECONE_API_KEY"] = pinecone_api_key
    st.session_state["PINECONE_ENVIRONMENT"] = environment