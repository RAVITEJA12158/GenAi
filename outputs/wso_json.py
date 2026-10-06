from pydantic import BaseModel, Field
from typing import Optional, Literal
from dotenv import load_dotenv
load_dotenv()
model=ChatHuggingFace(llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",  
    task="text-generation"
))
json_for={
    "title": "Person",
    "description": "A model representing a person with name, age, summary, and review.",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "The name of the person."
        },
        "age": {
            "type": "string",
            "description": "The age of the person."
        },
        "summary": {
            "type": "string",
            "description": "This is a summary of the person."
        },
        "review": {
            "type": "string",
            "enum": ["Positive", "Negative"],
            "description": "This is a review of the person."
        }
    },  
}



# here we can access the atteibutes by directly with the .name or if we want we can converrt it in to dic by dict(result) and to json model_dump_json