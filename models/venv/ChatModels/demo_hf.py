from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
lm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",
    task="text-generation"
)
hf=ChatHuggingFace(llm=lm)
print(hf.invoke("Briefly explain me gen aiin simple?"))
