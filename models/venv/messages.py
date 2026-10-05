from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
lm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",
    task="text-generation"
)
model=ChatHuggingFace(llm=lm)
messages = [
    SystemMessage(content="You are a helpful assistant.")
]
while True:
    user_input=input("You: ")
    if user_input.lower() == "exit":
        break
    messages.append(HumanMessage(content=user_input))
    model_response=model.invoke(messages)
    print("Model:", model_response.content)
    messages.append(AIMessage(content=model_response.content))      

print("Conversation ended.")
print("Conversation history:")
for message in messages:
    if isinstance(message, SystemMessage):
        print("System:", message.content)
    elif isinstance(message, HumanMessage):
        print("You:", message.content)
    elif isinstance(message, AIMessage):
        print("Model:", message.content)
print("direct")
print(messages)