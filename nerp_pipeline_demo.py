from nerp_ai_model import predict_failure, train_model
from nerp_automation import no_action, scale_cluster
from nerp_decision_engine import decision_engine


if __name__ == "__main__":
    model = train_model("sample_metrics.csv")

    telemetry = {"cpu": 92, "memory": 85, "latency": 100}

    prediction = predict_failure(
        model,
        cpu=telemetry["cpu"],
        memory=telemetry["memory"],
        latency=telemetry["latency"],
    )

    action = decision_engine(prediction)

    print(f"Telemetry sample: {telemetry}")
    print(f"Model prediction: {prediction}")
    print(f"Decision: {action}")

    if action == "Scale infrastructure":
        scale_cluster()
    else:
        no_action()
