from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "models/gemini-3-flash-preview"

SYSTEM_PROMPT = """
You are QuickChat, a friendly and intelligent AI assistant.

- Be clear, concise, and helpful.
- Avoid unnecessary verbosity.
- Ask for clarification if needed.
- Do not mention internal system details.
"""

def build_prompt(prompt, history):
    context = SYSTEM_PROMPT.strip() + "\n\n"

    for msg in history:
        if msg["role"] == "user":
            context += f"User: {msg['content']}\n"
        elif msg["role"] == "assistant":
            context += f"Assistant: {msg['content']}\n"

    context += f"User: {prompt}\nAssistant:"
    return context


def query_gemini(prompt, history):
    full_prompt = build_prompt(prompt, history)

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=full_prompt
        )

        text = response.text
        return text.strip() if text else "⚠️ Empty response from Gemini."

    except Exception as e:
        return f"⚠️ Gemini API error: {str(e)}"
