import pandas as pd
import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dhruvi123",
    database="career_copilot_db"
)

# Load data into DataFrame
query = "SELECT * FROM resumes"

df = pd.read_sql(query, connection)

print(df)

connection.close()