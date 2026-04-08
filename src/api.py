from fastapi import FastAPI
from pydantic import BaseModel
from src.model_loader import predict_score
from src.database import save_prediction

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Career Copilot API is running"}


class Candidate(BaseModel):
    resume_id: int
    experience: int
    projects: int


@app.post("/predict-score")
def get_prediction(data: Candidate):

    score = predict_score(
        data.experience,
        data.projects
    )

    if score >= 60:
        decision = "Selected"
    else:
        decision = "Rejected"

    save_prediction(
        data.resume_id,
        score,
        decision
    )

    return {
        "ai_score": score,
        "recruiter_decision": decision,
        "message": "Prediction stored successfully"
    }

