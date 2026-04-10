import joblib

# Load model
model = joblib.load("ai_score_model.pkl")

# Take input from user
experience_years = float(input("Enter experience (years): "))
projects_count = int(input("Enter number of projects: "))

# Predict
prediction = model.predict(
    [[experience_years, projects_count]]
)

print("\nPredicted AI Score:", round(prediction[0], 2))