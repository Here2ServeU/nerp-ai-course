"""
Day 4 — Training Your First Machine Learning Model
NERP AI Fundamentals

Loads the system metrics dataset, trains a Decision Tree classifier,
and makes a prediction on a new telemetry sample.
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# ---------------------------------------------------------------------------
# 1. Load dataset
# ---------------------------------------------------------------------------
DATA_PATH = "datasets/system_metrics.csv"

data = pd.read_csv(DATA_PATH)

print("Dataset Preview:")
print(data)
print()

# ---------------------------------------------------------------------------
# 2. Define features and label
# ---------------------------------------------------------------------------
FEATURE_COLUMNS = ["cpu_usage", "memory_usage"]
TARGET_COLUMN = "system_status"

X = data[FEATURE_COLUMNS]
y = data[TARGET_COLUMN]

# ---------------------------------------------------------------------------
# 3. Create and train the model
# ---------------------------------------------------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

print("Model trained successfully.\n")

# ---------------------------------------------------------------------------
# 4. Make a prediction on a new telemetry sample
# ---------------------------------------------------------------------------
# cpu_usage=92, memory_usage=85 -> likely warning/failure system state
sample = pd.DataFrame([{"cpu_usage": 92, "memory_usage": 85}])
prediction = model.predict(sample[FEATURE_COLUMNS])

print("Sample  : cpu_usage=92, memory_usage=85")
print(f"Prediction: {prediction[0]}")
