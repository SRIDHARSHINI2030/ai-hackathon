from app.gemini_service import generate_response
from app.session_memory import learning_session


def generate_adaptive_response(
    question: str,
    learner_answer: str,
    evaluation: str,
    next_action: dict,
    sources: list[dict],
) -> str:
    learner_level = learning_session.learner_level
    language = learning_session.language
    available_minutes = learning_session.available_minutes
    learning_objective = learning_session.learning_objective
    context = "\n\n".join(
        f"Source {index}: {item['text']}"
        for index, item in enumerate(sources, start=1)
    )

    prompt = f"""You are an AI Teacher continuing a learning session.

Use only the provided learning material.
Do not invent information that is not supported by the material.

The learner was asked:
{question}

The learner answered:
{learner_answer}

Evaluation of the learner's answer:
{evaluation}

Teaching decision:
{next_action["next_action"]}

Instruction:
{next_action["instruction"]}

Learning material:
{context}

Now continue teaching the learner.
Learner profile:
- Level: {learner_level}
- Language: {language}
- Available time: {available_minutes} minutes
- Learning objective: {learning_objective}

If the answer was incorrect, re-explain the concept simply and ask one new basic question.

If the answer was partially correct, explain what was missing using a different example or analogy and ask one new understanding question.

If the answer was correct, congratulate the learner briefly and ask a slightly more challenging question or introduce the next concept.

Keep the response clear, supportive, and suitable for a learner.
"""

    return generate_response(prompt)