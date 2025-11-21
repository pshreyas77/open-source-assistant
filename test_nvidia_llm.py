import os
from dotenv import load_dotenv

load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("="*60)
print("LLM INITIALIZATION TEST")
print("="*60)

print(f"\nAPI Keys Status:")
print(f"  NVIDIA_API_KEY: {'[SET]' if NVIDIA_API_KEY else '[NOT SET]'}")
print(f"  GOOGLE_API_KEY: {'[SET]' if GOOGLE_API_KEY else '[NOT SET]'}")
print(f"  OPENAI_API_KEY: {'[SET]' if OPENAI_API_KEY else '[NOT SET]'}")

print("\n" + "-"*60)
print("Testing NVIDIA LLM...")
print("-"*60)

if NVIDIA_API_KEY:
    try:
        from langchain_nvidia_ai_endpoints import ChatNVIDIA
        
        print("\n[1] Initializing NVIDIA ChatNVIDIA...")
        llm = ChatNVIDIA(
            model="meta/llama-3.1-8b-instruct",
            api_key=NVIDIA_API_KEY,
            temperature=0.7,
        )
        print("  [OK] Initialization successful")
        
        print("\n[2] Testing with a simple question...")
        question = "What is Python? Give a very short answer."
        response = llm.invoke(question)
        
        print(f"  [OK] LLM Response received")
        print(f"\n  Question: {question}")
        if hasattr(response, 'content'):
            print(f"  Answer: {response.content[:150]}...")
        else:
            print(f"  Answer: {str(response)[:150]}...")
        
        print("\n[SUCCESS] NVIDIA LLM IS WORKING!")
        
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")
        print(f"\nFull error details:")
        import traceback
        traceback.print_exc()
else:
    print("\n[ERROR] NVIDIA_API_KEY is not set in .env file")

print("\n" + "="*60)
