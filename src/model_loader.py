import pickle
import pandas as pd

# Load model once
with open("models/ai_score_model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_score(
    experience,
    skills_count,
    projects,
    cert_count,
    education_score
):

    features = pd.DataFrame(
        [[
            experience,
            skills_count,
            projects,
            cert_count,
            education_score
        ]],
        columns=[
            "experience",
            "skills_count",
            "projects",
            "cert_count",
            "education_score"
        ]
    )

    prediction = model.predict(features)[0]

    # Clip score to 0–100
    score = max(
        0,
        min(100, round(prediction, 2))
    )

    return score