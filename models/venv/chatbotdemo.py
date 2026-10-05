from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
lm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",
    task="text-generation"
)
model=ChatHuggingFace(llm=lm)
# generally the model does not have the ability to remember the previous conversation, so we need to implement a loop to keep the conversation going. Here is an example of how to do that:
# keep a list or dict to store the conversation history, and pass it to the model as context for each new input. so in the onvole we nned ot pass the lis tor the dict adn the rsult shoudl also be added and the problem when we use the list is the the model cannot understand the message theta thsi si given by the user or the ai so in dict we shoudl explicityly meantio nthe user and the ai so that the model can understand the context of the conversation. 
# langchain has identified this problem
while True:
    user_input=input("User: ")
    if user_input.lower() == "exit":
        break
    response=model.invoke(user_input)
    print("Model:", response.content)       