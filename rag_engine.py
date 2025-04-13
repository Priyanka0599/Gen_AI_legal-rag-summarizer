
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import openai

model = SentenceTransformer("all-MiniLM-L6-v2")

def split_text(text, chunk_size=500):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def build_faiss_index(chunks):
    vectors = model.encode(chunks)
    index = faiss.IndexFlatL2(len(vectors[0]))
    index.add(np.array(vectors).astype("float32"))
    return index, vectors, chunks

def retrieve_relevant_chunks(query, index, vectors, chunks, k=3):
    query_vec = model.encode([query]).astype("float32")
    D, I = index.search(query_vec, k)
    return [chunks[i] for i in I[0]]

def ask_gpt(query, context, client):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"..."}],
        temperature=0.3
    )
