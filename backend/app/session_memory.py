class LearningSession:
    def __init__(self):
        self.topic = None
        self.learner_level = None
        self.learning_objective = None
        self.language = None
        self.available_minutes = None
        self.history = []

    def start_session(
        self,
        topic: str,
        learner_level: str,
        learning_objective: str,
        language: str,
        available_minutes: int,
    ):
        self.topic = topic
        self.learner_level = learner_level
        self.learning_objective = learning_objective
        self.language = language
        self.available_minutes = available_minutes

    def add_interaction(
        self,
        question: str,
        learner_answer: str,
        evaluation: str,
        next_action: dict,
    ):
        self.history.append(
            {
                "question": question,
                "learner_answer": learner_answer,
                "evaluation": evaluation,
                "next_action": next_action,
            }
        )

    def get_history(self) -> list[dict]:
        return self.history

    def get_session_summary(self) -> dict:
        total_interactions = len(self.history)

        correct_count = 0
        partially_correct_count = 0
        incorrect_count = 0

        for interaction in self.history:
            evaluation = interaction["evaluation"].lower()

            if "partially correct" in evaluation:
                partially_correct_count += 1
            elif "incorrect" in evaluation:
                incorrect_count += 1
            elif "correct" in evaluation:
                correct_count += 1

        if total_interactions > 0:
          progress_percentage = round(
        (
            correct_count
            + (partially_correct_count * 0.5)
        )
        / total_interactions
        * 100
        )
        else:
           progress_percentage = 0
        return {
            "topic": self.topic,
            "learner_level": self.learner_level,
            "learning_objective": self.learning_objective,
            "language": self.language,
            "available_minutes": self.available_minutes,
            "interaction_count": total_interactions,
            "correct_count": correct_count,
            "partially_correct_count": partially_correct_count,
            "incorrect_count": incorrect_count,
            "progress_percentage": progress_percentage,
        }
learning_session = LearningSession()