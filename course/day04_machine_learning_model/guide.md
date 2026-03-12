
# NERP AI Fundamentals
## Day 4 — Training Your First Machine Learning Model

Welcome to **Day 4** of the NERP AI Fundamentals series.

In the previous lessons we built the foundation for understanding Artificial Intelligence.

Day 1: Environment setup  
Day 2: What Artificial Intelligence really is  
Day 3: Datasets and features  

Today we take the next step:

**Training your first Machine Learning model.**

---

# Objective

In this lesson you will:

- Load a dataset
- Train a simple machine learning model
- Make a prediction using system metrics

This example simulates a simplified concept used in the **NERP platform (Naweji Enterprise Reliability Platform)**.

NERP analyzes infrastructure signals such as:

- CPU usage
- memory usage
- system logs
- network activity

AI models learn patterns from this data to detect potential system risks.

---

# Project Structure

Your project should now look like this:

```
nerp-ai/
├── .venv/
├── datasets/
│   └── system_metrics.csv
├── train_model.py
└── guide.md
```

---

# Step 1: Activate Your Python Virtual Environment

Move to your project directory.

```
cd nerp-ai
```

Activate the virtual environment.

### Windows

```
.venv\Scripts\activate
```

### Linux or macOS

```
source .venv/bin/activate
```

You should see something like:

```
(.venv)
```

This means the virtual environment is active.

---

# Step 2: Install Machine Learning Libraries

Install required packages.

```
pip install pandas scikit-learn
```

Explanation:

| Library | Purpose |
|------|------|
| pandas | Data analysis and dataset loading |
| scikit-learn | Machine learning models |

---

# Step 3: Verify the Dataset

Check that the dataset exists:

```
datasets/system_metrics.csv
```

Example dataset:

```
cpu_usage,memory_usage,system_status
45,60,normal
50,65,normal
70,70,normal
85,75,warning
90,80,warning
95,85,failure
98,90,failure
```

Explanation:

| Column | Meaning |
|------|------|
| cpu_usage | CPU percentage |
| memory_usage | Memory percentage |
| system_status | Health state of the system |

---

# Step 4: Create the Training Script

Create a new file:

```
train_model.py
```

Add the following code:

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("datasets/system_metrics.csv")

# Features
X = data[["cpu_usage", "memory_usage"]]

# Target label
y = data["system_status"]

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Test prediction
prediction = model.predict([[92, 85]])

print("Prediction:", prediction)
```

---

# Step 5: Run the Model

Run the script from your terminal.

```
python train_model.py
```

Example output:

```
Prediction: ['warning']
```

This means the model predicts that the system metrics indicate a **warning state**.

---

# What Just Happened?

The machine learning model:

1. Loaded the dataset
2. Learned patterns from system metrics
3. Predicted the system state for new data

Even though this dataset is small, the concept is the same for large systems.

In production environments, AI models analyze millions of telemetry events to detect anomalies.

---

# How This Connects to NERP

The **NERP platform** will eventually analyze real infrastructure signals such as:

- Kubernetes metrics
- cloud infrastructure telemetry
- application logs
- financial transaction patterns
- healthcare system events

Machine learning models will detect patterns and identify risks before failures occur.

This enables **predictive reliability engineering**.

---

# Troubleshooting

### pandas not installed

```
pip install pandas
```

### scikit-learn not installed

```
pip install scikit-learn
```

### Dataset file not found

Verify the file exists:

```
datasets/system_metrics.csv
```

---

# Cleanup (Optional)

Deactivate the virtual environment.

```
deactivate
```

---

# Next Lesson

**Day 5: Model Evaluation and Accuracy**

In the next lesson you will learn:

- how to measure model accuracy
- how to validate machine learning models
- how to improve predictions

NERP AI Fundamentals continues on Day 5. See you then!


