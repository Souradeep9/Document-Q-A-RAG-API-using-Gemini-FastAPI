import os
import faiss
import numpy as np
from google import genai
from dotenv import load_dotenv
from app.embeddings import create_embedding
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
documents=[
    """
    Artificial Intelligence is the field of creating systems
    that can perform tasks requiring human intelligence.
    """,

    """
    Machine Learning is a subset of Artificial Intelligence
    where algorithms learn patterns from data.
    """,

    """
    Retrieval Augmented Generation combines information retrieval
    with large language models to generate grounded answers.
    """
]
embeddings=np.array([create_embedding(doc) for doc in documents],dtype="float32")
index=faiss.IndexFlatL2(embeddings.shape[1])
index.addython(embeddings)
def retrieve_documents(query,k=2):
    query_embeddings=create_embedding(query)
    distances,indices=index.search(np.array([query_embeddings]),k)
    results=[]
    for idx in indices[0]:
        results.append(documents[idx])
        return results
def generate_answer(query):
    retrieved_docs=retrieve_documents(query)
    context="\n\n".join(retrieved_docs)
    prompt=f"""
You are a helpful RAG assistant.

Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}

If the answer is not available in the context,
say "I don't have enough information."

Answer:
"""
    response=client.models.generate_content(
        model="gimi-3.7-flash",
        contents=prompt
    )
    return {
        "answar":response.text,
        "sources":retrieved_docs
    }