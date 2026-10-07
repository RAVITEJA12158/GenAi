from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model=ChatHuggingFace(llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4.1-Flash",  
    task="text-generation"
))
template=PromptTemplate(
    template=""""""

)
branch_chain=RunnableBranch(
    # (condition,chian)
    (lambda x: x.variable == "", chain),
    # for default there may be no chain so we use the Runnablelamda
    RunnableLambda(lambda x: 'default case')
)