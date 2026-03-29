"""
Day 6 — AI Decision Engine
NERP AI Fundamentals

Combines a prediction model and an anomaly detector to produce
a deterministic operational decision for each telemetry sample.
"""

import sys
from pathlib import Path

# Allow running this script directly from the course directory.
ROOT_DIR = Path(__file__).resolve().parents[0]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from nerp.ai_engine.anomaly_detector import detect_anomaly, train_anomaly_detector
from nerp.ai_engine.predict import predict_failure
from nerp.ai_engine.train_model import train_prediction_model
from nerp.decision_engine.decision_logic import decision_engine

# ---------------------------------------------------------------------------
# 1. Train models directly from the sample dataset
# ---------------------------------------------------------------------------
prediction_model = train_prediction_model()
anomaly_detector = train_anomaly_detector()

# ---------------------------------------------------------------------------
# 2. Define telemetry samples to evaluate
# ---------------------------------------------------------------------------
SAMPLES = [
    {"cpu": 92, "memory": 85, "latency": 110},
    {"cpu": 45, "memory": 48, "latency": 18},
    {"cpu": 60, "memory": 70, "latency": 40},
]

# ---------------------------------------------------------------------------
# 3. Run the decision engine for each sample
# ---------------------------------------------------------------------------
for i, sample in enumerate(SAMPLES, start=1):
    cpu = sample["cpu"]
    memory = sample["memory"]
    latency = sample["latency"]

    prediction = predict_failure(prediction_model, cpu=cpu, memory=memory, latency=latency)
    anomaly = detect_anomaly(anomaly_detector, cpu=cpu, memory=memory, latency=latency)
    action = decision_engine(prediction=prediction, anomaly_detected=anomaly)

    label = "failure risk" if prediction == 1 else "healthy"
    print(f"--- Sample {i}: cpu={cpu}, memory={memory}, latency={latency} ---")
    print(f"Prediction      : {prediction} ({label})")
    print(f"Anomaly detected: {anomaly}")
    print(f"Decision        : {action}")
    print()
