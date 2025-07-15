import os
import pandas as pd

# Load the data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sample.csv")

df = pd.read_csv(csv_path)

# Group by service and sum cost
grouped = df.groupby("service")["cost"].sum()

print("💰 Total Cost Per Service:")
print(grouped)