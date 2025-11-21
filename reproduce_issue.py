import os
from dotenv import load_dotenv
import traceback
import sys

# Redirect stdout and stderr to a file
log_file = open("reproduction.log", "w")
sys.stdout = log_file
sys.stderr = log_file

load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print(f"NVIDIA_API_KEY present: {bool(NVIDIA_API_KEY)}")
print(f"GOOGLE_API_KEY present: {bool(GOOGLE_API_KEY)}")

print("\n--- Testing NVIDIA LLM Initialization ---")
try:
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    llm = ChatNVIDIA(
        model="meta/llama-3.1-8b-instruct",
        api_key=NVIDIA_API_KEY,
        temperature=0.7,
    )
    print("[OK] NVIDIA LLM initialized successfully")
    # Try a simple invocation to ensure it actually works
    try:
        print("Attempting invocation...")
        response = llm.invoke("Hello")
        print(f"Invocation success: {response}")
    except Exception as e:
        print(f"Invocation failed: {e}")
        traceback.print_exc()

except Exception as e:
    print(f"NVIDIA LLM init error: {e}")
    traceback.print_exc()

print("\n--- Testing Google Gemini LLM Initialization ---")
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.7,
    )
    print("[OK] Google Gemini LLM initialized successfully")
    try:
        print("Attempting invocation...")
        response = llm.invoke("Hello")
        print(f"Invocation success: {response}")
    except Exception as e:
        print(f"Invocation failed: {e}")
        traceback.print_exc()
except Exception as e:
    print(f"Google LLM init error: {e}")
    traceback.print_exc()

log_file.close()
