import requests
import json

print("="*60)
print("TESTING OPEN SOURCE ASSISTANT CHAT API")
print("="*60)

tests = [
    {
        "name": "Basic Question",
        "question": "What is Python?"
    },
    {
        "name": "GitHub Search Query",
        "question": "Find me popular Python machine learning projects"
    },
    {
        "name": "Programming Help",
        "question": "How can I contribute to open source?"
    }
]

url = 'http://127.0.0.1:5000/api/chat'

for i, test in enumerate(tests, 1):
    print(f"\n[Test {i}/{len(tests)}] {test['name']}")
    print("-" * 60)
    
    payload = {
        "conversation_id": f"test_{i}",
        "question": test['question']
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ SUCCESS (Status: {response.status_code})")
            print(f"\nQuestion: {test['question']}")
            print(f"\nAnswer: {data.get('answer', 'No answer provided')[:200]}...")
            
            if 'context_data' in data and data['context_data'].get('repositories'):
                repos = data['context_data']['repositories']
                print(f"\n  Found {len(repos)} repositories:")
                for repo in repos[:3]:
                    print(f"   - {repo['name']} ({repo['stars']} stars)")
        else:
            print(f"✗ FAILED (Status: {response.status_code})")
            print(f"Error: {response.text[:200]}")
            
    except requests.exceptions.Timeout:
        print("✗ TIMEOUT: Request took too long")
    except Exception as e:
        print(f"✗ ERROR: {type(e).__name__}: {str(e)[:100]}")

print("\n" + "="*60)
print("TEST COMPLETE")
print("="*60)
