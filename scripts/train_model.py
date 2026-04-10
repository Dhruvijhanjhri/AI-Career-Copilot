import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

print("Loading dataset...")

# Load dataset
df = pd.read_csv("data/cleaned_resumes.csv")

print("Dataset loaded successfully")
print("Total records:", len(df))


# ==============================
# FEATURE ENGINEERING
# ==============================

print("Creating features...")

# Count skills
df["skills_count"] = df["Skills"].apply(
    lambda x: len(str(x).split(","))
)

# Experience
df["experience"] = df["Experience (Years)"].fillna(0)

# Projects
df["projects"] = df["Projects Count"].fillna(0)

# Certifications count
df["cert_count"] = df["Certifications"].apply(
    lambda x: len(str(x).split(","))
)

# Education mapping
df["education_score"] = df["Education"].map({
    "High School": 1,
    "Bachelor": 2,
    "Master": 3,
    "PhD": 4
})

df["education_score"] = df["education_score"].fillna(2)


# ==============================
# TARGET VARIABLE
# ==============================

print("Preparing target...")

y = df["AI Score (0-100)"].clip(0, 100)


# ==============================
# FEATURES
# ==============================

X = df[
    [
        "experience",
        "skills_count",
        "projects",
        "cert_count",
        "education_score"
    ]
]


# ==============================
# SPLIT DATA
# ==============================

print("Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==============================
# TRAIN MODEL
# ==============================

print("Training model...")

model = LinearRegression()

model.fit(
    X_train,
    y_train
)


# ==============================
# EVALUATE MODEL
# ==============================

predictions = model.predict(X_test)

predictions = [
    max(0, min(100, p))
    for p in predictions
]
mae = mean_absolute_error(
    y_test,
    predictions
)

print("Model evaluation completed")
print("MAE:", round(mae, 2))


# ==============================
# SAVE MODEL
# ==============================

print("Saving model...")

with open(
    "models/ai_score_model.pkl",
    "wb"
) as f:

    pickle.dump(
        model,
        f
    )

print("Model saved successfully")