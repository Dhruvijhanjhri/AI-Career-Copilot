import joblib

# Load trained model
model = joblib.load("models/ai_score_model.pkl")

def predict_score(experience, projects):
    
    features = [[experience, projects]]
    
    prediction = model.predict(features)
    
    return int(prediction[0])