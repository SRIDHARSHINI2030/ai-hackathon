import requests

from video.video_generator import generate_video


BACKEND_URL = "http://127.0.0.1:8000"


def ask_backend(question, top_k=3):
    response = requests.post(
        f"{BACKEND_URL}/ask",
        json={
            "question": question,
            "top_k": top_k
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    answer = data.get("answer", "").strip()

    if not answer:
        raise RuntimeError(
            f"Backend returned no answer: {data}"
        )

    return answer


def build_video_script_from_backend(lesson_plan):
    topic = lesson_plan.get("topic", "the topic")
    learner_level = lesson_plan.get(
        "learner_level",
        "beginner"
    )
    learning_objective = lesson_plan.get(
        "learning_objective",
        ""
    )
    language = lesson_plan.get(
        "language",
        "English"
    )
    lesson_steps = lesson_plan.get(
        "lesson_steps",
        []
    )

    prompt = f"""
Create a complete beginner-friendly lesson about "{topic}".

Learner level: {learner_level}
Learning objective: {learning_objective}
Language: {language}

Use ONLY the uploaded learning material as your source.

Return the lesson using exactly these six headings:

INTRODUCTION:
A friendly 1-2 sentence introduction.

CONCEPT_EXPLANATION:
A clear, detailed step-by-step explanation of the topic.

EXAMPLE:
One simple example or demonstration based on the learning material.

QUESTION:
One simple question for the learner. Return only the question.

UNDERSTANDING_CHECK:
A short check that asks the learner to recall the key idea.

CONCLUSION:
A concise summary of the most important points.

Keep the language suitable for the learner level.
"""

    answer = ask_backend(prompt)

    sections = {
        "INTRODUCTION": "",
        "CONCEPT_EXPLANATION": "",
        "EXAMPLE": "",
        "QUESTION": "",
        "UNDERSTANDING_CHECK": "",
        "CONCLUSION": "",
    }

    current_section = None

    for line in answer.splitlines():
        cleaned = line.strip()

        matched_section = None

        for section_name in sections:
            heading = section_name + ":"

            if cleaned.upper() == heading:
                matched_section = section_name
                break

        if matched_section:
            current_section = matched_section
            continue

        if current_section and cleaned:
            if sections[current_section]:
                sections[current_section] += " " + cleaned
            else:
                sections[current_section] = cleaned

    # Fallback if Gemini does not follow the requested format.
    if not sections["CONCEPT_EXPLANATION"]:
        sections["CONCEPT_EXPLANATION"] = answer

    if not sections["INTRODUCTION"]:
        sections["INTRODUCTION"] = (
            f"Hello! Today we are going to learn about {topic}."
        )

    if not sections["EXAMPLE"]:
        sections["EXAMPLE"] = (
            f"Let's look at an example of {topic}."
        )

    if not sections["QUESTION"]:
        sections["QUESTION"] = (
            f"What is the main idea behind {topic}?"
        )

    if not sections["UNDERSTANDING_CHECK"]:
        sections["UNDERSTANDING_CHECK"] = (
            f"Pause and recall the key idea you learned about {topic}."
        )

    if not sections["CONCLUSION"]:
        sections["CONCLUSION"] = (
            f"Let's review the main ideas we learned about {topic}."
        )

    segments = []

    for step in lesson_steps:

        if step == "Introduction":
            segments.append({
                "section": "Introduction",
                "spoken_text": sections["INTRODUCTION"],
                "visual": f"Introduction to {topic}"
            })

        elif step == "Concept explanation":
            segments.append({
                "section": "Concept explanation",
                "spoken_text": sections["CONCEPT_EXPLANATION"],
                "visual": (
                    f"Step-by-step educational explanation "
                    f"of {topic}"
                )
            })

        elif step == "Example or demonstration":
            segments.append({
                "section": "Example or demonstration",
                "spoken_text": sections["EXAMPLE"],
                "visual": (
                    f"Real-world example demonstrating {topic}"
                )
            })

        elif step == "Questions for the learner":
            segments.append({
                "section": "Questions for the learner",
                "spoken_text": (
                    "Now, let me ask you a question. "
                    + sections["QUESTION"]
                ),
                "visual": sections["QUESTION"]
            })

        elif step == "Understanding check":
            segments.append({
                "section": "Understanding check",
                "spoken_text": sections["UNDERSTANDING_CHECK"],
                "visual": sections["UNDERSTANDING_CHECK"]
            })

        elif step == "Conclusion":
            segments.append({
                "section": "Conclusion",
                "spoken_text": sections["CONCLUSION"],
                "visual": f"Summary of {topic}"
            })

    return {
        "topic": topic,
        "language": language,
        "segments": segments
    }

def generate_video_from_backend_lesson_plan(
    lesson_plan,
    output_path="video/lesson_video.mp4"
):
    video_script = build_video_script_from_backend(
        lesson_plan
    )

    generate_video(
        video_script,
        output_path
    )


if __name__ == "__main__":
    demo_lesson_plan = {
        "topic": "Matrix Addition in Java",
        "learner_level": "beginner",
        "learning_objective": (
            "Understand how matrix addition works using arrays in Java"
        ),
        "language": "English",
        "available_minutes": 10,
        "lesson_steps": [
            "Introduction",
            "Concept explanation",
            "Example or demonstration",
            "Questions for the learner",
            "Understanding check",
            "Conclusion"
        ]
    }

    generate_video_from_backend_lesson_plan(
        demo_lesson_plan
    )
    generate_video_from_backend_lesson_plan(
        demo_lesson_plan
    )