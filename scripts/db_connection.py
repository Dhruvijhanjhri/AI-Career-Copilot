import mysql.connector

# Step 1: Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dhruvi123",
    database="career_copilot_db"
)

# Step 2: Check connection
if connection.is_connected():
    print("Connected to MySQL database")

# Step 3: Close connection
connection.close()