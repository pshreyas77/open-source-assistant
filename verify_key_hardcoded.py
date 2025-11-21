import requests
import os

# Hardcoded key from the file view to ensure no dotenv issues
key = "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"

print(f"Key being tested: {key[:10]}...{key[-5:]}")

url = "https://integrate.api.nvidia.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}
payload = {
    "model": "meta/llama-3.1-8b-instruct",
    "messages": [{"role": "user", "content": "Hello"}],
    "temperature": 0.7,
    "max_tokens": 10,
    "stream": False
}

try:
    response = requests.post(url, headers=headers, json=payload, timeout=10)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Success! The key is valid.")
    else:
        print(f"Failed: {response.text}")
except Exception as e:
    print(f"Error: {e}")
