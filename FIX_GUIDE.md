# Backend Chat Fix - Configuration Guide

## Current Issue
The application is returning a `500 Chat error` with details `404 models/g...`. This error occurs because:

1. **Google Gemini API Access Issue**: Your Google API key doesn't have access to the Gemini models (gemini-pro, gemini-1.5-pro, gemini-1.5-flash)
2. **Possible Causes**:
   - The API key might be from a different Google service (e.g., Maps, YouTube)
   - The Generative AI API might not be enabled for your Google Cloud project
   - Billing might not be enabled
   - The models might not be available in your region

## Solutions (Choose ONE)

### Option 1: Fix Google API Access (RECOMMENDED if you want to use Gemini)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a NEW API key specifically for Generative AI
3. Make sure "Generative Language API" is enabled
4. Update your `.env` file with the new key:
   ```
   GOOGLE_API_KEY=your_new_api_key_here
   ```

### Option 2: Use OpenAI Instead (EASIEST FIX)

1. Get an OpenAI API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Add it to your `.env` file:
   ```
   OPENAI_API_KEY=sk-...your_key_here
   ```
3. The app will automatically use OpenAI as a fallback!

### Option 3: Test with Dummy LLM (For Testing Only)

If you just want to test the application without real AI:
1. Temporarily remove or comment out your GOOGLE_API_KEY in `.env`:
   ```
   # GOOGLE_API_KEY=...
   ```
2. The app will use a dummy LLM that returns a clear error message

## Next Steps After Configuration

1. **Restart the Flask server**:
   ```
   Stop the current server (Ctrl+C)
   python app.py
   ```

2. **Test the configuration**:
   ```
   python check_config.py
   ```
   This will show which API keys are working.

3. **Test the chat endpoint**:
   ```
   python test_chat.py
   ```

## Current Status

✅ Flask server is running
✅ API routes are configured correctly
✅ Code structure is clean and functional
❌ LLM connection needs valid API key

---

**What would you like to do?**
1. Get a new Google Generative AI key?
2. Add an OpenAI API key instead?
3. Something else?
