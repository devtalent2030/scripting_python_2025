import os

"""


# Check if a file exists, This prevents crashing your script if the file is missing.
if os.path.exists("usage.csv"):
    print("File found.")
else:
    print("File not found.")


# Get the current working directory
cwd = os.getcwd()
print("Current folder:", cwd)


# Build safe file paths (cross-platform)
filename = "usage.csv"
file_path = os.path.join(os.getcwd(), filename)
print("Full path:", file_path)

# List files in a folder
files = os.listdir(".")
print("Files in this folder:", files)

# Delete a file (careful!)
if os.path.exists("old_report.csv"):
    os.remove("old_report.csv")

"""

file = "usage.csv"

print("📂 Current folder:", os.getcwd())
print("📄 Does usage.csv exist?", os.path.exists(file))
print("📂 All files here:", os.listdir("."))

if os.path.exists(file):
    print("✅ We found the file. Ready to analyze.")
else:
    print("🚫 File is missing. Please upload or check the filename.")