from langchain_openai import OpenAiEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = OpenAiEmbeddings(model="text-embedding-3-large",dimensions=3072)