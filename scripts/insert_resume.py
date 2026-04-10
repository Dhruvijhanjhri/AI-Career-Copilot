import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dhruvi123",
    database="career_copilot_db"
)

cursor = connection.cursor()

query = """
INSERT INTO resumes (
    name,
    email,
    phone,
    education,
    experience_years,
    job_role,
    projects_count,
    salary_expectation
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

data = (
    "Dhruvi Jhanjhri",
    "dhruvi@email.com",
    "9876543210",
    "MSc Data Science",
    1.5,
    "Data Scientist",
    5,
    600000
)

cursor.execute(query, data)

connection.commit()

print("Data inserted successfully")

cursor.close()
connection.close()