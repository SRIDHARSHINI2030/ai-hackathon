from fastapi import FastAPI

from app.lesson_planner import create_lesson_plan
from app.models import LessonPlanRequest
from app.material_router import router as material_router
from app.question_models import QuestionRequest
from app.rag_service import generate_grounded_answer


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


@app.post("/ask")
def ask_question(request: QuestionRequest):
    return generate_grounded_answer(
        question=request.question,
        top_k=request.top_k,
    )


app.include_router(material_router)