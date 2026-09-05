from app.retrieval_service import retrieve_relevant_chunks
from app.gemini_service import generate_response


def evaluate_learner_answer(
    question: str,
    learner_answer: str,
    top_k: int = 3,
) -> dict:
    relevant_chunks = retrieve_relevant_chunks(question, top_k=top_k)

    if not relevant_chunks:
        return {
            "evaluation": "I could not find relevant information in the uploaded learning material.",
            "sources": [],
        }

    context = "\n\n".join(
        f"Source {index}: {item['text']}"
        for index, item in enumerate(relevant_chunks, start=1)
    )

    prompt = f"""You are an AI Teacher evaluating a learner's answer.

Use only the provided learning material to evaluate the answer.
Do not invent facts that are not supported by the material.

Determine whether the learner's answer is:
- Correct
- Partially correct
- Incorrect

Then provide:
1. The result
2. What the learner understood correctly
3. What is missing or incorrect
4. A short, constructive explanation to help the learner improve

Learning material:
{context}

Question:
{question}

Learner answer:
{learner_answer}
"""

    evaluation = generate_response(prompt)

    return {
        "evaluation": evaluation,
        "sources": relevant_chunks,
    }