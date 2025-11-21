from dotenv import load_dotenv
import os

# Force reload
load_dotenv(override=True)

nvidia_key = os.getenv("NVIDIA_API_KEY")
print(f"NVIDIA_API_KEY present: {bool(nvidia_key)}")
if nvidia_key:
    print(f"Key starts with: {nvidia_key[:10]}...")
else:
    print("NVIDIA_API_KEY is missing!")
