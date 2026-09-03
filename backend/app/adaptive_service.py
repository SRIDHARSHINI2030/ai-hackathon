def decide_next_action(evaluation: str) -> dict:
    evaluation_lower = evaluation.lower()

    if "partially correct" in evaluation_lower:
        return {
            "result": "partially_correct",
            "next_action": "re_explain",
            "instruction": "Explain the missing concept using a different example, then ask a new understanding question.",
        }

    if "incorrect" in evaluation_lower:
        return {
            "result": "incorrect",
            "next_action": "re_teach",
            "instruction": "Re-explain the concept in a simpler way, then ask a new basic question.",
        }

    if "correct" in evaluation_lower:
        return {
            "result": "correct",
            "next_action": "advance",
            "instruction": "Congratulate the learner and move to a slightly more challenging question or the next concept.",
        }

    return {
        "result": "unknown",
        "next_action": "clarify",
        "instruction": "Ask the learner to clarify their answer before continuing.",
    }