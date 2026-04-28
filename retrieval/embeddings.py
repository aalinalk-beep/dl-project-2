from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts):
    embeddings = model.encode(texts)
    return embeddings


if __name__ == "__main__":
    sample_texts = [
        "Transformers are powerful",
        "BERT is used for understanding",
        "GPT is used for generation"
    ]

    vectors = embed_texts(sample_texts)

    for i, vec in enumerate(vectors):
        print(f"Text: {sample_texts[i]}")
        print(f"Vector length: {len(vec)}")
        print("-" * 50)