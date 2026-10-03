from langchain_openai import OpenAiEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()
embeddings = OpenAiEmbeddings(model="text-embedding-3-large", dimensions=3072)
docuemnts = [
    "The capital of France is Paris.", 
     "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers." 
]
document_embeddings = embeddings.embed_documents(docuemnts)
query = "Who is the best Indian cricketer?"
query_embedding = embeddings.embed_query(query)
cosi=cosine_similarity([query_embedding], document_embeddings) 
print(cosi)