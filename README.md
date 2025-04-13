# 🧾 Legal Document Summarizer with RAG + GPT

A Streamlit-based AI tool that helps users quickly summarize lengthy legal documents, extract key clauses, and flag risky sections. Built using Retrieval-Augmented Generation (RAG) with OpenAI's GPT and Sentence-BERT for embedding.

---

## 🚀 Features

- 📄 Upload `.txt` or `.pdf` legal documents
- 🧠 Uses **RAG** to ground GPT responses in real document content
- ✍️ Summarizes documents in plain English
- ⚖️ Extracts confidentiality, risk, and compliance clauses
- 🔐 Users enter their own OpenAI API key (secure + free for you!)
- 🧩 Powered by:
  - FAISS (vector search)
  - Sentence-Transformers
  - OpenAI GPT-3.5 Turbo

---

## 🛠️ How It Works (RAG)

1. 🔹 **Split** uploaded document into smaller chunks
2. 🔹 **Embed** each chunk using Sentence-BERT
3. 🔹 **Index** those embeddings using FAISS
4. 🔹 **Retrieve** top-matching chunks based on user query
5. 🔹 **Generate** an answer using GPT-3.5 with the retrieved context

---

## 🧪 Demo Prompts

- `Summarize this agreement in bullet points`
- `What are the confidentiality clauses?`
- `Are there any risky or compliance-related terms?`
- `Explain the termination clause simply`

---

## 📦 Installation (for local testing)

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
