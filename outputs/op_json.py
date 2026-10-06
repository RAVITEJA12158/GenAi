from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
model=ChatHuggingFace(llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",  
    task="text-generation"
))
parser = JsonOutputParser()
template=PromptTemplate(
    template="""You are a helpful assistant. explain about {topic} in JSON format with keys 'title' and 'description'{format_instructions}.""",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
pr=template.format(topic="Cricket")
result=model.invoke(pr)
par=parser.parse(result.content)
print(result)
print(par)
# or direclty call chain=template | model | parser and invoke and thats it no need to call the format and parse methods separately.
# but the drawback is there is no schema enforcement
