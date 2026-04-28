def fixed_size_chunking(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        
        start += chunk_size - overlap
    
    return chunks


def sentence_chunking(text, max_chunk_size=300):
    sentences = text.split(". ")
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + ". "
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks


if __name__ == "__main__":
    sample_text = "This is a test. Deep learning is powerful. Transformers changed NLP. Attention is all you need."
    
    print("FIXED SIZE:")
    print(fixed_size_chunking(sample_text))
    
    print("\nSENTENCE BASED:")
    print(sentence_chunking(sample_text))