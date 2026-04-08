import joblib
import mysql.connector

# Load trained model
model = joblib.load("ai_score_model.pkl")

# Connect to database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dhruvi123",
    database="career_copilot_db"
)

cursor = connection.cursor()

# Take user input
resume_id = int(input("Enter Resume ID: "))
experience_years = float(input("Enter experience (years): "))
projects_count = int(input("Enter number of projects: "))

# Predict AI score
prediction = model.predict(
    [[experience_years, projects_count]]
)

ai_score = int(round(prediction[0]))

# Simple recruiter decision logic
if ai_score >= 60:
    decision = "Selected"
else:
    decision = "Rejected"

predicted_role = "Data Scientist"

# Insert into predictions table
query = """
INSERT INTO predictions (
    resume_id,
    predicted_role,
    ai_score,
    recruiter_decision
)
VALUES (%s, %s, %s, %s)
"""

data = (
    resume_id,
    predicted_role,
    ai_score,
    decision
)

cursor.execute(query, data)

connection.commit()

print("\nPrediction stored successfully")
print("AI Score:", ai_score)
print("Recruiter Decision:", decision)

cursor.close()
connection.close()