
import streamlit as st
import PyPDF2
from rag_engine import split_text, build_faiss_index, retrieve_relevant_chunks, ask_gpt
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="🧾 Legal RAG Summarizer", layout="wide")
st.title("Legal Document Summarizer (with RAG)")

uploaded_file = st.file_uploader("Upload a legal document (.txt or .pdf)", type=["txt", "pdf"])

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    return "".join([page.extract_text() for page in reader.pages])

if uploaded_file:
    raw_text = uploaded_file.read().decode("utf-8") if uploaded_file.name.endswith(".txt") else extract_text_from_pdf(uploaded_file)
    st.subheader("Preview (first 1000 characters)")
    st.write(raw_text[:1000])

    with st.spinner("Processing document with RAG..."):
        chunks = split_text(raw_text)
        index, vectors, all_chunks = build_faiss_index(chunks)

    query = st.text_input("🔍 Ask something about the document, or type 'summarize'")

    if query:
        with st.spinner("Retrieving relevant sections..."):
            retrieved = retrieve_relevant_chunks(query, index, vectors, all_chunks)
            context = "\n\n".join(retrieved)
            response = ask_gpt(query, context)
            st.markdown("### 📝 Response")
            st.write(response)
    