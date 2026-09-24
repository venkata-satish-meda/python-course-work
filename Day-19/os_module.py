import os

print("Current folder:", os.getcwd())
print("Python file name:", os.path.basename(__file__))

# Create a folder only when it does not exist.
folder = "practice_output"
os.makedirs(folder, exist_ok=True)
print("Folder ready:", os.path.exists(folder))
