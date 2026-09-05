def create_lesson_plan(
    topic: str,
    learner_level: str,
    learning_objective: str,
    language: str,
    available_minutes: int,
):
    if available_minutes <= 5:
        lesson_steps = [
            "Quick introduction",
            "Key concept explanation",
            "One simple example",
            "Quick understanding check",
            "Conclusion",
        ]

    elif available_minutes <= 20:
        lesson_steps = [
            "Introduction",
            "Concept explanation",
            "Example or demonstration",
            "Questions for the learner",
            "Understanding check",
            "Conclusion",
        ]

    else:
        lesson_steps = [
            "Introduction and prior knowledge check",
            "Concept explanation",
            "Detailed examples",
            "Demonstration or application",
            "Questions for the learner",
            "Understanding check",
            "Misconception check",
            "Practice activity",
            "Summary and next steps",
        ]

    if learner_level.lower() == "beginner":
        teaching_approach = "Use simple explanations, basic examples, and step-by-step guidance."

    elif learner_level.lower() == "intermediate":
        teaching_approach = "Use moderate detail, practical examples, and application-based questions."

    elif learner_level.lower() == "advanced":
        teaching_approach = "Use deeper explanations, challenging examples, and application-based questions."

    else:
        teaching_approach = "Adapt explanations and examples to the learner's stated level."

    return {
        "topic": topic,
        "learner_level": learner_level,
        "learning_objective": learning_objective,
        "language": language,
        "available_minutes": available_minutes,
        "teaching_approach": teaching_approach,
        "lesson_steps": lesson_steps,
    }