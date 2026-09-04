from fastapi import FastAPI

from app.lesson_planner import create_lesson_plan
from app.models import LessonPlanRequest
from app.adaptive_service import decide_next_action
from app.adaptive_response_service import generate_adaptive_response
from app.evaluation_models import EvaluationRequest
from app.evaluation_service import evaluate_learner_answer
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


@app.post("/adaptive-teach")
def adaptive_teach(request: EvaluationRequest):
    evaluation_result = evaluate_learner_answer(
        question=request.question,
        learner_answer=request.learner_answer,
        top_k=request.top_k,
    )

    next_action = decide_next_action(
        evaluation_result["evaluation"]
    )

    adaptive_response = generate_adaptive_response(
        question=request.question,
        learner_answer=request.learner_answer,
        evaluation=evaluation_result["evaluation"],
        next_action=next_action,
        sources=evaluation_result["sources"],
    )

    return {
        "evaluation": evaluation_result["evaluation"],
        "next_action": next_action,
        "adaptive_response": adaptive_response,
        "sources": evaluation_result["sources"],
    }