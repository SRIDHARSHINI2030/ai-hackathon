from fastapi import FastAPI
from app.lesson_planner import create_lesson_plan
from app.models import LessonPlanRequest

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Teacher Backend is running"
    }


@app.post("/lesson-plan")
def lesson_plan(request: LessonPlanRequest):
    return create_lesson_plan(
        topic=request.topic,
        learner_level=request.learner_level,
        learning_objective=request.learning_objective,
        language=request.language,
        available_minutes=request.available_minutes,
    )