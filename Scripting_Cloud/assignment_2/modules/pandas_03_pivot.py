import os
import pandas as pd

# Load the data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sample.csv")

df = pd.read_csv(csv_path)

# Create a pivot table: rows = date, columns = service, values = cost
pivot = df.pivot_table(index="date", columns="service", values="cost", aggfunc="sum")

print("📊 Daily Service Costs:")
print(pivot)

# Calculate percent change (spike detection)
spikes = pivot.pct_change() * 100

print("\n⚠️ Percent Change Day Over Day:")
print(spikes.round(2))