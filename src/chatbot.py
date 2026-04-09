def chatbot_response(message):

    message = message.lower()

    if "job" in message:
        return "You can try roles like Data Scientist or Software Engineer."

    elif "salary" in message:
        return "Data Scientists earn around 12 LPA on average."

    elif "skills" in message:
        return "Python, SQL, and Machine Learning are in high demand."

    elif "hello" in message:
        return "Hello! How can I assist you today?"

    else:
        return "I'm here to help with career guidance."