from fastapi import FastAPI
from app.lesson_planner import create_lesson_plan

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Teacher Backend is running"
    }


@app.get("/lesson-plan")
def lesson_plan():
    return create_lesson_plan(
        topic="Photosynthesis",
        learner_level="Beginner",
        learning_objective="Understand the basic process of photosynthesis",
        language="English",
        available_minutes=20,
    )