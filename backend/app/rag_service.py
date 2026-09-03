from app.retrieval_service import retrieve_relevant_chunks
from app.gemini_service import generate_response


def generate_grounded_answer(question: str, top_k: int = 3) -> dict:
    relevant_chunks = retrieve_relevant_chunks(question, top_k=top_k)

    if not relevant_chunks:
        return {
            "answer": "I could not find relevant information in the uploaded learning material.",
            "sources": [],
        }

    context = "\n\n".join(
        f"Source {index}: {item['text']}"
        for index, item in enumerate(relevant_chunks, start=1)
    )

    prompt = f"""You are an AI Teacher. Answer the learner question using only the provided learning material. Do not invent information that is not supported by the material. If the material does not contain enough information to answer the question, say so clearly. Explain the answer in a clear, learner-friendly way.

Learning material:
{context}

Learner question:
{question}"""

    answer = generate_response(prompt)

    return {
        "answer": answer,
        "sources": relevant_chunks,
    }