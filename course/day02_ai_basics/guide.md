
# AI Fundamentals in 7 Days
## Day 2 — What Artificial Intelligence Really Is

**Created by Emmanuel Naweji, 2026**

Welcome to **Day 2** of the *AI Fundamentals in 7 Days* learning journey.

Yesterday we prepared our development environment and installed the tools that will allow us to experiment with Artificial Intelligence.

Today we explore an important concept:

**What Artificial Intelligence really is.**

Artificial Intelligence is the ability for a system to **learn patterns from data and use those patterns to make predictions or decisions**.

Computers do not think like humans.  
Instead, they analyze data and discover patterns that help predict what may happen next.

This process is called **Machine Learning**.

---

# Machine Learning

Machine Learning is a branch of Artificial Intelligence where algorithms **learn from data instead of being explicitly programmed**.

### Traditional Programming

Engineers write rules directly.

```cmd
IF temperature > 80
THEN turn_on_cooling_system
```

The engineer defines the rule.

### Machine Learning

Instead of writing rules, we provide many examples.

The algorithm studies the examples and learns the rule automatically.

Example data:

- normal system behavior
- system failures

The model learns patterns that indicate when a failure may occur.

This is the intelligence we want inside the **NERP platform**.

---

# Artificial Intelligence in NERP

The **Naweji Enterprise Reliability Platform (NERP)** observes systems such as:

- cloud infrastructure
- financial platforms
- healthcare systems

By analyzing system data, NERP can detect patterns such as:

- unusual CPU usage
- abnormal transaction behavior
- unusual network activity

These patterns allow the system to **predict risks and trigger responses**.

---

# The Three Core Components of Machine Learning

## 1. Data

Data is the information the system learns from.

Examples:

- system logs
- performance metrics
- financial transactions
- user activity

## 2. The Model

The model is the mathematical structure that learns patterns from data.

Different models solve different problems:

- predictions
- classifications
- anomaly detection

## 3. Predictions

Once a model learns patterns, it can predict outcomes for new data.

Examples:

- predicting server failure
- detecting suspicious transactions
- identifying abnormal system behavior

These predictions eventually power **automation systems inside NERP**.

---

# Hands-On Practice

Activate your virtual environment.

### Mac / Linux

```cmd
source .venv/bin/activate
```

### Windows

```cmd
.venv\Scripts\activate
```

Your terminal should show:

```cmd
(.venv)
```

---

Verify installed libraries.

```cmd
pip list
```

You should see:

- numpy
- pandas
- scikit-learn

---

# Create a Simple Dataset

Create a dataset folder.

```cmd
mkdir datasets
```

Create a dataset file.

```cmd
touch datasets/system_metrics.csv
```

Example dataset:

```
cpu_usage,memory_usage,system_status
45,60,normal
50,65,normal
90,80,warning
95,85,failure
```

This data will later train a machine learning model.

---

# Assignment

1. Activate your virtual environment
2. Verify installed libraries
3. Create a dataset folder
4. Create a system_metrics.csv dataset

Understanding data is the **first step toward building intelligent systems**.

---

# Next Lesson

In **Day 3**, we will explore:

**Features and datasets**.

You will learn how raw data becomes input for machine learning models.

See you in **Day 3**.
