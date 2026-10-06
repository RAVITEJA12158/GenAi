from pydantic import BaseModel, Field
from typing import Optional, Literal
from dotenv import load_dotenv
load_dotenv()
model=ChatHuggingFace(llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",  
    task="text-generation"
))
class Person(BaseModel):
    name: str = Field(..., description="The name of the person.")
    age: str = Field(..., description="The age of the person.")
    summary: str = Field(..., description="This is a summary of the person.")
    review: Literal["Positive", "Negative"] = Field(..., description="This is a review of the person.")


# here we can access the atteibutes by directly with the .name or if we want we can converrt it in to dic by dict(result) and to json model_dump_json