import os

file_path = "credentials.json"
if os.path.exists(file_path):
    print("File found! ✅")
else:
    print("File not found ❌")
