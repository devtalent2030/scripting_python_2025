import os
import pandas as pd

# Dynamically get the path to the CSV file
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sample.csv")

df = pd.read_csv(csv_path)

print("✅ Loaded Data:")
print(df)