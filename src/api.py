from fastapi import FastAPI
from pydantic import BaseModel
from src.model_loader import predict_score
from src.database import save_prediction
from src.job_recommender import recommend_job
from src.salary_service import get_salary
from src.chatbot import chatbot_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Career Copilot API is running"}


class Candidate(BaseModel):
    resume_id: int
    experience: int
    skills_count: int
    projects: int
    cert_count: int
    education_score: int

class SkillInput(BaseModel):
    skills: str

class ChatInput(BaseModel):
    message: str

@app.post("/predict-score")
def get_prediction(data: Candidate):

    print("STEP 1: Request received")

    score = predict_score(
        data.experience,
        data.skills_count,
        data.projects,
        data.cert_count,
        data.education_score
    )

    print("STEP 2: Score calculated:", score)

    if score >= 75:
        decision = "Accepted"

    elif score >= 50:
        decision = "Shortlisted"

    else:
        decision = "Rejected"

    print("STEP 3: Decision made:", decision)

    save_prediction(
        data.resume_id,
        score,
        decision
    )

    print("STEP 4: Saved to database")

    return {
        "ai_score": score,
        "recruiter_decision": decision,
        "message": "Prediction stored successfully"
    }

@app.post("/recommend-job")
def get_job_recommendation(data: SkillInput):

    job = recommend_job(data.skills)

    return {
        "recommended_job": job
    }

@app.get("/salary-insights")
def salary_insights(role: str):

    salary = get_salary(role)

    return {
        "role": role,
        "average_salary": salary
    }

@app.post("/chat")
def chat(data: ChatInput):

    response = chatbot_response(data.message)

    return {
        "user_message": data.message,
        "bot_response": response
    }