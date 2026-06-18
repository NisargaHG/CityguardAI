import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("data/events.csv")

# Keep useful columns
df = df[
    [
        "event_type",
        "event_cause",
        "status",
        "zone",
        "priority"
    ]
]

# Remove missing rows
df = df.dropna()

# Encode categorical columns
encoders = {}

for col in df.columns:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    encoders[col] = le

# Features
X = df[
    [
        "event_type",
        "event_cause",
        "status",
        "zone"
    ]
]

# Target
y = df["priority"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
acc = model.score(X_test, y_test)

print("Accuracy:", acc)

# Save
joblib.dump(model, "models/risk_model.pkl")
joblib.dump(encoders, "models/encoders.pkl")

print("Model Saved")