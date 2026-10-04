from json import load

from langchain_core.prompts import PromptTemplate
from langchain_core.load import loads
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
load_dotenv()
model=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
st.header("Prompt Template")
st.text_input("Enter the input language:", key="input_language")
st.text_input("Enter the output language:", key="output_language")                                                                              
if st.button("Generate Prompt"):
    with open("template.json", "r") as f:
        loaded_template = loads(f.read())
    prompt=loaded_template.invoke({
        'input_language': st.session_state.input_language,
        'output_language': st.session_state.output_language
    })
    result=model.invoke(prompt)
    st.write("Generated Prompt:")
    st.write(prompt.to_string())
    st.write("Generated Response:")
    st.write(result)