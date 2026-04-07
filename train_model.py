import pandas as pd
import mysql.connector
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Connect to database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dhruvi123",
    database="career_copilot_db"
)

# Load data
query = "SELECT * FROM resumes"
df = pd.read_sql(query, connection)

connection.close()

# Create AI Score manually (temporary logic)
df["ai_score"] = (
    df["experience_years"] * 10
    + df["projects_count"] * 5
)

# Features
X = df[["experience_years", "projects_count"]]

# Target
y = df["ai_score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "ai_score_model.pkl")

print("Model trained and saved successfully")