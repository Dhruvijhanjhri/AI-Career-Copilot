import mysql.connector

def save_prediction(resume_id, score, decision):

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dhruvi123",
        database="career_copilot_db"
    )

    cursor = connection.cursor()

    query = """
    INSERT INTO predictions
    (resume_id, ai_score, recruiter_decision)
    VALUES (%s, %s, %s)
    """

    values = (
        resume_id,
        score,
        decision
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()