from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from dotenv import load_dotenv
load_dotenv()
model=ChatHuggingFace(llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",  
    task="text-generation"
))
schema = [
    ResponseSchema(name="name", description="The name of the person."), 
    ResponseSchema(name="age", description="The age of the person."),
    ResponseSchema(name="summary", description="This is a summary of the person."),
]
parser = StructuredOutputParser.from_response_schemas(schema)
template=PromptTemplate(    
    
    template="""You are a helpful assistant. explain about {topic} in JSON format with keys 'name', 'age' and 'summary'{format_instructions}.""",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
# rest is same as the json output parser and the only difference is that it will validate the output and if the output is not in the correct format it will raise an error.