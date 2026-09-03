from app.text_chunker import chunk_text
from app.embedding_service import create_embeddings
from app.vector_store import VectorStore


vector_store = VectorStore()


def process_material(text: str):
    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)

    vector_store.add(chunks, embeddings)

    return {
        "chunk_count": len(chunks),
        "message": "Material processed and stored successfully",
    }