from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate       
load_dotenv()
model=ChatHuggingFace(llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",  
    task="text-generation"
))
parser = StrOutputParser()
template = PromptTemplate.from_template("""You are a helpful assistant. Please provide a brief summary of the following text in one sentence.
Text: {topic}""")

template1 = PromptTemplate.from_template("""You are a worst assistant. Please provide a brief summary of the following text in one sentence.
Text: {text}""")
chain = template | model | parser | template1 | model | parser
result = chain.invoke({"topic":"Cricket"})
print(result)
