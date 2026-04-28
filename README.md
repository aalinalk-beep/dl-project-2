# 🤖 Deep Learning RAG Chatbot

A full Retrieval-Augmented Generation (RAG) chatbot built from scratch for answering Deep Learning questions using local documents.

---

## 🚀 Project Overview

This project implements a complete RAG pipeline:

* Document ingestion (PDF, DOCX)
* Chunking (fixed-size and sentence-based)
* Embeddings using Sentence Transformers (BERT-based)
* Vector search using FAISS
* Retrieval of top-k relevant chunks
* Answer generation using a local LLM (LLaMA 3 via Ollama)
* Streamlit-based chat interface

The system generates answers grounded in retrieved context and includes source citations.

---

## 🧠 Technologies Used

* Python
* Sentence Transformers (`all-MiniLM-L6-v2`)
* FAISS (vector database)
* Ollama (LLaMA 3 local LLM)
* Streamlit

---

## 📂 Project Structure

```
dl2-chatbot/
├── data/              
├── ingest/            
├── retrieval/         
├── generation/        
├── ui/                
├── eval/              
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

### 1. Clone repository

```
git clone <your-repo-link>
cd dl2-chatbot
```

### 2. Create virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🤖 Running the Project

### Start Ollama

```
ollama serve
```

### Run chatbot

```
streamlit run ui/app.py
```

---

## 📥 Data

Place Deep Learning documents in:

```
data/
```

Supported formats:

* PDF
* DOCX

---

## 🔍 System Architecture

```
User → Query → Embedding → FAISS → Top-k Chunks → LLM → Answer
```

---

## 📊 Evaluation Results

* Dataset: 30 QA pairs
* Retrieval metric: Precision@5
* Result: **0.93**

The system demonstrates strong retrieval performance and semantic understanding.

---

## 🧪 Experiment Log

Key improvements:

* Increased chunk size → improved context coverage
* Increased overlap → reduced information loss
* Sentence-based chunking → better semantic quality
* Increased top-k → improved recall

---

## ⚠️ Limitations

* Retrieval errors for complex queries
* Chunking may split important context
* Local LLM is slower than cloud models

---

## 🔬 Future Work

* Hybrid retrieval (BM25 + embeddings)
* Advanced chunking strategies
* RAGAS evaluation metrics
* Deployment as a web service

---

## 📌 Author

Alina Amangeldieva
Deep Learning Course Project

---

## 💡 Key Insight

* **BERT-style models** → embeddings (understanding)
* **GPT-style models** → generation (text output)

Together they form modern RAG systems.
