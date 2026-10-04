from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
lm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",
    task="text-generation"
)
model=ChatHuggingFace(llm=lm)
while True:
    user_input=input("User: ")
    if user_input.lower() == "exit":
        break
    response=model.invoke(user_input)
    print("Model:", response)       