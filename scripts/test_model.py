import pickle
import pandas as pd

print("Loading model...")

# Load model
with open(
    "models/ai_score_model.pkl",
    "rb"
) as f:

    model = pickle.load(f)

print("Model loaded successfully")


# ==============================
# TEST INPUTS
# ==============================

test_data = pd.DataFrame(
    [
        [1, 2, 0, 0, 2],
        [3, 4, 1, 1, 2],
        [6, 6, 3, 2, 3],
        [10, 10, 5, 3, 4]
    ],
    columns=[
        "experience",
        "skills_count",
        "projects",
        "cert_count",
        "education_score"
    ]
)

print("\nTest inputs:")
print(test_data)


# ==============================
# PREDICT
# ==============================

predictions = model.predict(test_data)

print("\nPredictions:")

for i, score in enumerate(predictions):

    # Clip score to 0–100
    score = max(0, min(100, round(score, 2)))

    if score >= 75:
        decision = "Accepted"

    elif score >= 50:
        decision = "Shortlisted"

    else:
        decision = "Rejected"

    print(
        f"Candidate {i+1}: {score} | {decision}"
    )