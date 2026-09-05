from app.embedding_service import create_embeddings
from app.material_pipeline import vector_store


def retrieve_relevant_chunks(query: str, top_k: int = 3):
    query_embedding = create_embeddings([query])[0]

    results = vector_store.search(query_embedding, top_k=top_k)

    return [
        {
            "score": float(score),
            "text": chunk,
        }
        for score, chunk in results
    ]