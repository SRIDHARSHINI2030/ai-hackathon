def create_lesson_plan(
    topic: str,
    learner_level: str,
    learning_objective: str,
    language: str,
    available_minutes: int,
):
    return {
        "topic": topic,
        "learner_level": learner_level,
        "learning_objective": learning_objective,
        "language": language,
        "available_minutes": available_minutes,
        "lesson_steps": [
            "Introduction",
            "Concept explanation",
            "Example or demonstration",
            "Questions for the learner",
            "Understanding check",
            "Conclusion",
        ],
    }