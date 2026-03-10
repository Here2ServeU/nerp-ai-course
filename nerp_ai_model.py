import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_model(csv_path: str = "sample_metrics.csv") -> RandomForestClassifier:
    df = pd.read_csv(csv_path)

    x = df[["cpu", "memory", "latency"]]
    y = df["failure"]

    model = RandomForestClassifier(random_state=42)
    model.fit(x, y)
    return model


def predict_failure(model: RandomForestClassifier, cpu: int, memory: int, latency: int) -> int:
    sample = pd.DataFrame(
        [{"cpu": cpu, "memory": memory, "latency": latency}]
    )
    prediction = model.predict(sample)
    return int(prediction[0])


if __name__ == "__main__":
    model = train_model()
    prediction = predict_failure(model, cpu=92, memory=85, latency=100)
    print(f"Prediction: [{prediction}]")
