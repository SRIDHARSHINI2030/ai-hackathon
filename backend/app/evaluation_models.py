from pydantic import BaseModel


class EvaluationRequest(BaseModel):
    question: str
    learner_answer: str
    top_k: int = 3