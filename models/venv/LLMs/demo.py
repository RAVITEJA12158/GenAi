from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm=OpenAI(model='gpt-4.1')
result=llm.invoke("Describe gen ai")
print(result)