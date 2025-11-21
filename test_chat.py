import requests
import json

url = 'http://127.0.0.1:5000/api/chat'
payload = {
    "conversation_id": "test",
    "question": "What is Python?"
}

try:
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print(f"\nFull Response Text:")
    print(response.text)
    
    if response.status_code == 200:
        print("\n✓ SUCCESS! Chat is working!")
        data = response.json()
        if 'answer' in data:
            print(f"\nAnswer: {data['answer']}")
    else:
        print(f"\n✗ ERROR: Got status code {response.status_code}")
        try:
            error_data = response.json()
            print(f"Error details: {json.dumps(error_data, indent=2)}")
        except:
            print(f"Raw error: {response.text}")
            
except requests.exceptions.ConnectionError:
    print("✗ ERROR: Cannot connect to server. Is Flask running on port 5000?")
except Exception as e:
    print(f"✗ ERROR: {type(e).__name__}: {e}")
