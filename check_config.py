import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 60)
print("API KEY STATUS CHECK")
print("=" * 60)

# Check all API keys
google_key = os.getenv("GOOGLE_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")
github_token = os.getenv("GITHUB_TOKEN")
nvidia_key = os.getenv("NVIDIA_API_KEY")
openrouter_key = os.getenv("OPENROUTER_API_KEY")

print(f"\nGOOGLE_API_KEY: {'[OK] Set' if google_key else '[X] NOT SET'}")
if google_key:
    print(f"  Length: {len(google_key)} characters")
    print(f"  Starts with: {google_key[:10]}...")

print(f"\nOPENAI_API_KEY: {'[OK] Set' if openai_key else '[X] NOT SET'}")
if openai_key:
    print(f"  Length: {len(openai_key)} characters")
    print(f"  Starts with: {openai_key[:10]}...")

print(f"\nGITHUB_TOKEN: {'[OK] Set' if github_token else '[X] NOT SET'}")
print(f"NVIDIA_API_KEY: {'[OK] Set' if nvidia_key else '[X] NOT SET'}")
print(f"OPENROUTER_API_KEY: {'[OK] Set' if openrouter_key else '[X] NOT SET'}")

print("\n" + "=" * 60)
print("TESTING LLM INITIALIZATION")
print("=" * 60)

# Test Google LLM
if google_key:
    print("\n[1] Testing Google Gemini LLM...")
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key=google_key,
            temperature=0.7,
        )
        print("  [OK] Google LLM initialized successfully")
        
        # Try a simple invoke
        try:
            response = llm.invoke("Say 'test successful'")
            print(f"  [OK] Test message successful: {response.content[:50]}...")
        except Exception as e:
            print(f"  [ERROR] Test message failed: {str(e)[:100]}")
    except Exception as e:
        print(f"  [ERROR] Google LLM initialization failed: {str(e)[:150]}")
else:
    print("\n[1] [SKIP] Skipping Google LLM test (no API key)")

# Test OpenAI LLM
if openai_key:
    print("\n[2] Testing OpenAI LLM...")
    try:
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=openai_key,
            temperature=0.7,
        )
        print("  [OK] OpenAI LLM initialized successfully")
        
        # Try a simple invoke
        try:
            response = llm.invoke("Say 'test successful'")
            print(f"  [OK] Test message successful: {response.content[:50]}...")
        except Exception as e:
            print(f"  [ERROR] Test message failed: {str(e)[:100]}")
    except Exception as e:
        print(f"  [ERROR] OpenAI LLM initialization failed: {str(e)[:150]}")
else:
    print("\n[2] [SKIP] Skipping OpenAI LLM test (no API key)")

print("\n" + "=" * 60)
print("RECOMMENDATIONS")
print("=" * 60)

if not google_key and not openai_key:
    print("\n[WARNING] No LLM API keys are configured!")
    print("   Please set either GOOGLE_API_KEY or OPENAI_API_KEY in your .env file")
elif google_key and not openai_key:
    print("\n[OK] Google API key is set")
    print("  Consider adding OPENAI_API_KEY as a fallback")
elif openai_key and not google_key:
    print("\n[OK] OpenAI API key is set")
    print("  Consider adding GOOGLE_API_KEY as primary option")
else:
    print("\n[OK] Both API keys are configured (good for redundancy!)")

print("\n")
