# evaluate_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score, train_test_split 

# Loading the dataset 
DATA_PATH = "datasets/system_metrics.csv"
data = pd.read_csv(DATA_PATH)
print(f"Dataset shape: {data.shape}\n")

# Defining features and labels
FEATURE_COLUMNS = ["cpu_usage", "memory_usage"]
TARGET_LABELS = "system_status"

X = data[FEATURE_COLUMNS]
y = data[TARGET_LABELS]

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training samples : {len(X_train)}")
print(f"Testing samples : {len(X_test)}\n")

# Training the model on the training set
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluting the test set
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}\n")

print("Classification Report:")
print(classification_report(y_test, y_pred))

# Cross-validation for a more reliable estimate
min_class_count = y.value_counts().min()
cv_folds = min(5, min_class_count)

if cv_folds >= 2:
	cv_scores = cross_val_score(model, X, y, cv=cv_folds)
	print(f"Cross-Validation Scores ({cv_folds}-fold): {cv_scores}")
	print(f"Mean CV Accuracy : {cv_scores.mean():.2f}")
else:
	print("Cross-validation skipped: not enough samples per class for at least 2 folds.")
