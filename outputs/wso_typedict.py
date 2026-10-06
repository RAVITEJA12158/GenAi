from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Literal
load_dotenv()
lm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",  
    task="text-generation"
)
model=ChatHuggingFace(llm=lm)
class testing(TypedDict):
    name:str
    age:str
    summary:Annotated[str,"This is a summary of the person."]
    review:Annotated[Literal["Positive", "Negative"], "This is a review of the person."]
aftermodel=model.with_structured_output(testing)
result=aftermodel.invoke("""Anish is a 12 year old boy who loves to play football. He is very friendly and always helps his friends. He is also very good at academics and has won several awards in school competitions.""")   
print(result)                    


# the problem with this method is there is no validation of the output, if the model does not follow the structure of the TypedDict, it will still return the output without any error. This can lead to unexpected behavior and bugs in the code. It is important to validate the output of the model to ensure that it follows the expected structure and types.    