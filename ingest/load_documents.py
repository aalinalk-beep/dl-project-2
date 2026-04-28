from pypdf import PdfReader
from docx import Document
import os


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    filename = os.path.basename(file_path)

    return {
        "text": text,
        "metadata": {
            "source": filename,
            "title": os.path.splitext(filename)[0],
            "date": "unknown"
        }
    }


def load_docx(file_path):
    doc = Document(file_path)
    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    filename = os.path.basename(file_path)

    return {
        "text": text,
        "metadata": {
            "source": filename,
            "title": os.path.splitext(filename)[0],
            "date": "unknown"
        }
    }


def load_documents(data_folder):
    documents = []

    for file in os.listdir(data_folder):
        file_path = os.path.join(data_folder, file)

        if file.endswith(".pdf"):
            documents.append(load_pdf(file_path))

        elif file.endswith(".docx"):
            documents.append(load_docx(file_path))

    return documents


if __name__ == "__main__":
    docs = load_documents("data")

    for doc in docs:
        print("SOURCE:", doc["metadata"]["source"])
        print("TITLE:", doc["metadata"]["title"])
        print("DATE:", doc["metadata"]["date"])
        print("TEXT SAMPLE:", doc["text"][:200])
        print("=" * 50)