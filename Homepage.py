import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
#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

chat = None
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ""
else:
    chat = ChatOpenAI(openai_api_key = st.session_state["OPENAI_API_KEY"])

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ""

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ""

st.set_page_config(page_title="Welcome to ASL", layout="wide")
st.title("Welcome to ASL")

# with st.container():
#     st.header("OpenAI Setting")
#     st.markdown(f"""
#     ***API KEY:*** {st.session_state["OPENAI_API_KEY"]}
#     """)

# with st.container():
#     st.header("Pinecone Settings")
#     st.markdown(f"""
#     ***API KEY:*** {st.session_state["PINECONE_API_KEY"]}
#
#     ***Environment:*** {st.session_state["PINECONE_ENVIRONMENT"]}
#     """)

if chat:
    with st.container():
        st.header("Chat with GPT")
        prompt = st.text_input("Prompt",value="",type="default")
        asked = st.button("Ask")
        if asked:
            ai_message = chat([HumanMessage(content=prompt)])
            st.write(ai_message.content)

else:
    with st.container():
        st.warning("Please set the OpenAI API key before in the OpenAI page.")