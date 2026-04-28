import csv

from retrieval.vector_store import create_vector_store, search


def load_qa_dataset(file_path="eval/qa_dataset.csv"):
    dataset = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dataset.append({
                "question": row["question"],
                "expected_source": row["expected_source"],
                "ground_truth": row["ground_truth"]
            })

    return dataset


def evaluate_precision_at_5():
    index, chunks, metadata = create_vector_store()
    dataset = load_qa_dataset()

    correct = 0
    total = len(dataset)

    print("\n=== RETRIEVAL EVALUATION ===\n")

    for item in dataset:
        question = item["question"]
        expected_source = item["expected_source"]

        results = search(question, index, chunks, metadata, top_k=5)
        retrieved_sources = [r["source"] for r in results]

        is_correct = expected_source in retrieved_sources

        if is_correct:
            correct += 1

        print("Question:", question)
        print("Expected source:", expected_source)
        print("Retrieved sources:", retrieved_sources)
        print("Correct:", is_correct)
        print("-" * 80)

    precision_at_5 = correct / total

    print("\n=== FINAL RESULT ===")
    print(f"Correct: {correct}/{total}")
    print(f"Precision@5: {precision_at_5:.2f}")

    return precision_at_5


if __name__ == "__main__":
    evaluate_precision_at_5()