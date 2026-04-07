import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dhruvi123",
    database="career_copilot_db"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM resumes")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()