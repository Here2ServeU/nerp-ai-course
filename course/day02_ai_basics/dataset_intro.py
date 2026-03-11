import pandas as pd

data = {
    "cpu_usage": [45, 50, 90, 95],
    "memory_usage": [60, 65, 80, 85],
    "system_status": ["normal", "normal", "warning", "failure"]
}

df = pd.DataFrame(data)

print("Dataset Preview:")
print(df)
