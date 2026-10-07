from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

template1=PromptTemplate(
   
input_variables=[]
)
template2=PromptTemplate(
   
input_variables=[]
)

model=ChatHuggingFace(llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",  
    task="text-generation"
))
parser=StrOutputParser()
parllel_chain=RunnableParallel({
    'chain1':template1 | model | parser,
    'chain2':template2 | model | parser
})
chain = parllel_chain|template2|model

chain.get_graph().print_ascii()

