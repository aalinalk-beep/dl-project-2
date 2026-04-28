import faiss
import numpy as np

from ingest.load_documents import load_documents
from ingest.chunking import fixed_size_chunking
from retrieval.embeddings import embed_texts


def create_vector_store():
    documents = load_documents("data")

    all_chunks = []
    metadata = []

    for doc in documents:
        chunks = fixed_size_chunking(doc["text"])

        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            metadata.append({
                "source": doc["metadata"]["source"],
                "title": doc["metadata"]["title"],
                "date": doc["metadata"]["date"],
                "chunk_id": i
            })

    embeddings = embed_texts(all_chunks)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings).astype("float32"))

    return index, all_chunks, metadata


def search(query, index, chunks, metadata, top_k=5):
    query_vec = embed_texts([query])

    distances, indices = index.search(
        np.array(query_vec).astype("float32"),
        top_k
    )

    results = []

    for i in indices[0]:
        results.append({
            "text": chunks[i],
            "source": metadata[i]["source"],
            "title": metadata[i]["title"],
            "date": metadata[i]["date"],
            "chunk_id": metadata[i]["chunk_id"]
        })

    return results


if __name__ == "__main__":
    index, chunks, metadata = create_vector_store()

    query = "What is attention in transformers?"
    results = search(query, index, chunks, metadata)

    for r in results:
        print("SOURCE:", r["source"])
        print("TITLE:", r["title"])
        print("CHUNK:", r["chunk_id"])
        print("TEXT:", r["text"][:200])
        print("=" * 50)