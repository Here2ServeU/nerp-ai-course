# NERP AI Foundations

NERP (Naweji Enterprise Reliability Platform) is the applied reliability intelligence framework emerging from my PhD research and Cloud/Platform Engineering practice, designed to transform infrastructure telemetry into evidence-based, autonomous operational actions. In practice, NERP continuously observes system signals, applies machine learning for risk prediction, selects the optimal response policy, and executes automated remediation.

Beginner-friendly starter project for learning the core NERP intelligence loop:

**Telemetry -> AI Model -> Decision -> Automation**

This repository is intentionally small and practical. It demonstrates how infrastructure metrics can be converted into an automated operational action.

## Overview

Goal for this week:

1. Understand how a simple ML model learns from telemetry.
2. Predict risk from new metric values.
3. Convert predictions into decisions.
4. Trigger automation from those decisions.

Example flow:

- CPU spike detected.
- Model predicts failure risk.
- Decision engine chooses to scale.
- Automation runs scaling action.

## Architecture

```text
sample_metrics.csv -> nerp_ai_model.py -> nerp_decision_engine.py -> nerp_automation.py
                                   \______________________________________________/
                                              orchestrated by nerp_pipeline_demo.py
```

## Project Structure

- `nerp_ai_model.py`: trains and runs a basic Random Forest classifier.
- `nerp_decision_engine.py`: maps model output to an operational decision.
- `nerp_automation.py`: executes action handlers (safe print placeholders).
- `nerp_pipeline_demo.py`: full end-to-end orchestration.
- `sample_metrics.csv`: default training dataset used by scripts.
- `data/sample_metrics.csv`: dataset copy under `data/` for cleaner structure.

## Requirements

- Python 3.11+
- Dependencies in `requirements.txt`

Install:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

Run model only:

```bash
/Users/emmanuelnaweji/nerp-ai-beginner/.venv/bin/python nerp_ai_model.py
```

Run full pipeline:

```bash
/Users/emmanuelnaweji/nerp-ai-beginner/.venv/bin/python nerp_pipeline_demo.py
```

Expected output:

```text
Prediction: [1]
Telemetry sample: {'cpu': 92, 'memory': 85, 'latency': 100}
Model prediction: 1
Decision: Scale infrastructure
Scaling Kubernetes cluster
kubectl scale deployment api --replicas=6
```

## Script-by-Script Explanation

### `nerp_ai_model.py` (Model Layer)

- Reads telemetry dataset from CSV.
- Uses features: `cpu`, `memory`, `latency`.
- Uses label: `failure` (`0` healthy, `1` risk).
- Trains `RandomForestClassifier`.
- Predicts risk for new telemetry input.

Pitch line:
"This is the prediction brain. It learns patterns from historical metrics and classifies new telemetry as healthy or risky."

### `nerp_decision_engine.py` (Decision Layer)

- Accepts model prediction.
- Returns action text:
  - `1` -> `Scale infrastructure`
  - `0` -> `System healthy`

Pitch line:
"This translates AI output into a deterministic operational decision."

### `nerp_automation.py` (Automation Layer)

- Implements action handlers.
- Current implementation prints safe placeholder commands.
- Easy place to plug in real orchestration (`kubectl`, cloud SDKs, APIs).

Pitch line:
"This is the actuator that executes infrastructure response."

### `nerp_pipeline_demo.py` (Orchestration Layer)

- Trains model.
- Defines telemetry sample.
- Generates prediction.
- Gets decision.
- Executes matching automation path.

Pitch line:
"This script demonstrates the complete intelligence loop end-to-end."

## 60-Second Demo Narrative

"I built a starter NERP intelligence pipeline. The model learns from CPU, memory, and latency metrics to predict failure risk. A decision engine maps predictions to clear actions. An automation layer executes those actions. The pipeline script wires the complete flow from telemetry to infrastructure response."

## 7-Day Learning Plan (1-2 Hours/Day)

1. Day 1: Environment setup, dependencies, and dataset basics.
2. Day 2: Run and inspect `nerp_ai_model.py`.
3. Day 3: Learn anomaly detection basics (Isolation Forest).
4. Day 4: Extend rules in `nerp_decision_engine.py`.
5. Day 5: Add safe/real modes in `nerp_automation.py`.
6. Day 6: Test multiple telemetry scenarios.
7. Day 7: Present full pipeline demo with explanation.

## Next Professional Upgrades

1. Load telemetry from API input instead of hard-coded values.
2. Add model evaluation metrics (`accuracy`, `precision`, `recall`).
3. Add unit tests for decision and automation modules.
4. Add FastAPI endpoint for prediction and action simulation.
5. Add logging and alerting for production-style observability.

## Notes

- Keep this phase simple. Do not jump into advanced models yet.
- Mastering basic ML pipeline design is the best foundation for NERP.

---
***Keep learning ... Keep building.***
**By Emmanuel Naweji, 2026**


