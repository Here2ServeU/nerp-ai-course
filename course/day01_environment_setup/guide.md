# AI Fundamentals in 7 Days

## Day 1 --- Environment Setup and Prerequisites

**Created by Emmanuel Naweji, 2026**

Welcome to Day 1 of the AI Fundamentals in 7 Days learning journey.

In this program we explore the foundations of Artificial Intelligence
while building components of a real platform called the Naweji
Enterprise Reliability Platform (NERP).

NERP is designed to use Artificial Intelligence to predict and prevent
failures in complex systems, including cloud infrastructure, financial
platforms, and healthcare systems.

Over the next seven days we will learn the fundamentals of Artificial
Intelligence step by step in a simple and practical way.

Today we begin with the most important step: preparing our development
environment.

------------------------------------------------------------------------

## What You Need

To begin learning Artificial Intelligence, we need three things.

### 1. Python

Python is the most widely used programming language in Artificial
Intelligence.\
It is powerful, easy to learn, and supported by thousands of AI
libraries.

### 2. A Code Editor

You will need a code editor such as: - Visual Studio Code - PyCharm -
Sublime Text - Any editor you prefer

### 3. Machine Learning Libraries

We will use: - NumPy - Pandas - Scikit‑learn

These tools help us work with data and build machine learning models.

------------------------------------------------------------------------

## Step 1 --- Verify Python Installation

Open your terminal and run:

```sh
python3 --version
```

or

```sh
python --version
```

If Python is not installed, download it from:

```txt
https://python.org
```
Install Python 3.9 or newer.

------------------------------------------------------------------------

## Step 2 --- Create the Project Folder

Create the folder that will contain our AI experiments.

```sh
mkdir nerp_ai
cd nerp_ai
```
------------------------------------------------------------------------

## Step 3 --- Create a Virtual Environment

Virtual environments isolate dependencies for each project.

Mac / Linux

```sh
python3 -m venv .venv
```
Windows

```
python -m venv .venv
```
------------------------------------------------------------------------

## Step 4 --- Activate the Virtual Environment

Mac / Linux

```sh
source .venv/bin/activate
```
Windows
```
.venv`\Scripts`{=tex}`\activate`{=tex}
```
When activated your terminal will display:
```txt
(.venv)
```
------------------------------------------------------------------------

## Step 5 --- Install Machine Learning Libraries

```sh
pip install numpy pandas scikit-learn
```
------------------------------------------------------------------------

## Step 6 --- Create Your First Python Script

Create a file named:
```sh
touch ai_intro.py
```
Add the following code:
```txt
print("NERP AI environment ready")
```
Run the script:
```sh
python ai_intro.py
```
If the message appears, your AI environment is ready.

------------------------------------------------------------------------

## Your Assignment

Before Day 2:

1.  Install Python
2.  Create the nerp_ai project folder
3.  Create and activate the virtual environment
4.  Install the ML libraries
5.  Run the Python script

------------------------------------------------------------------------

## Next Lesson

In Day 2 we will explore:

What is Artificial Intelligence really?\
How do machines learn from data?
