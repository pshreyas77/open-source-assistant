import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print("Testing direct Google Generative AI connection...")
print("=" * 60)

if GOOGLE_API_KEY:
    try:
        import google.generativeai as genai
        
        genai.configure(api_key=GOOGLE_API_KEY)
        
        print("\n[1] Listing available models...")
        models = genai.list_models()
        print("\nAvailable models that support generateContent:")
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                print(f"  - {model.name}")
        
        print("\n[2] Testing with gemini-pro model...")
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Say 'Hello, this is a test'")
        print(f"  Response: {response.text}")
        print("  [OK] Direct API test successful!")
        
    except Exception as e:
        print(f"[ERROR] {str(e)}")
else:
    print("No GOOGLE_API_KEY found")
