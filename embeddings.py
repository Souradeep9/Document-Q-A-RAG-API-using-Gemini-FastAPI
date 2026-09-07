import os
import numpy as np
from dotenv import load_dotenv
from google import genai
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def create_embedding(text:str):
    response=client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return np.array(response.embeddings[0].values,dtype="float32")