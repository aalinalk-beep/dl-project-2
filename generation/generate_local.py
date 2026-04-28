from ollama import chat

from retrieval.vector_store import create_vector_store, search


def build_prompt(query, retrieved_chunks):
    context_parts = []

    for chunk in retrieved_chunks:
        context_parts.append(
            f"""
[Source: {chunk["source"]}]
[Title: {chunk["title"]}]
[Date: {chunk["date"]}]
[Chunk ID: {chunk["chunk_id"]}]

{chunk["text"]}
"""
        )

    context_text = "\n\n".join(context_parts)

    prompt = f"""
You are a Deep Learning course assistant.

Answer the question ONLY using the context below.

Rules:
1. Use only the provided context.
2. Cite the source document name for every factual claim.
3. If the answer is not supported by the context, say exactly:
"I cannot find this in the provided documents."
4. Do not invent information.

Context:
{context_text}

Question:
{query}

Answer:
"""
    return prompt


def generate_answer(query):
    index, chunks, metadata = create_vector_store()
    results = search(query, index, chunks, metadata, top_k=5)

    prompt = build_prompt(query, results)

    response = chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":
    question = "What is attention in transformers?"

    answer = generate_answer(question)
    print("\n=== ANSWER ===\n")
    print(answer)