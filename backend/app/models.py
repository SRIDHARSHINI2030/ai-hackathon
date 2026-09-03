from pydantic import BaseModel


class LessonPlanRequest(BaseModel):
    topic: str
    learner_level: str
    learning_objective: str
    language: str
    available_minutes: int