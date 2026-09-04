from app.gemini_service import generate_response


def generate_next_question(
    question: str,
    learner_answer: str,
    evaluation: str,
    next_action: dict,
    sources: list[dict],
) -> str:
    context = "\n\n".join(
        f"Source {index}: {item['text']}"
        for index, item in enumerate(sources, start=1)
    )

    prompt = f"""You are an AI Teacher continuing an interactive learning session.

Use only the provided learning material.
Do not invent information that is not supported by the material.

Previous question:
{question}

Learner's previous answer:
{learner_answer}

Evaluation:
{evaluation}

Teaching decision:
{next_action["next_action"]}

Learning material:
{context}

Generate exactly ONE new question for the learner.

Rules:
- If the learner was incorrect, ask a simple question that checks the basic concept again.
- If the learner was partially correct, ask a question that checks the missing part.
- If the learner was correct, ask a slightly more challenging question or move toward the next concept.
- Keep the question clear and concise.
- Do not provide the answer.
- Do not ask multiple questions.
- Use only information supported by the learning material.

Return only the new question.
"""

    return generate_response(prompt)