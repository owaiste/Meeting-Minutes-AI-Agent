import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Load local environment variables
load_dotenv()

# Check .env file first, otherwise try a direct text string backup
api_key = os.getenv("GEMINI_API_KEY")

# ⚠️ MANUALLY PASTE YOUR KEY HERE IF YOUR .ENV FILE HAS A TYPO
if not api_key or api_key == "your_actual_api_key_here":
    api_key = "AIzaSy..." # <-- Paste your real 39-character key directly here as a backup!

if not api_key or api_key.startswith("your_"):
    raise ValueError("Missing or invalid GEMINI_API_KEY! Please check your key setup.")

# 2. Initialize the official Google GenAI Client
client = genai.Client(api_key=api_key)

# 3. Read input workspace files
with open("sample_transcript.txt", "r") as f:
    transcript = f.read()

with open("SKILL.md", "r") as f:
    skill_instructions = f.read()

# 4. Define the Agent Prompts and Day 4 Security Guardrails
system_instruction = f"""
You are an executive administrative assistant agent. 
{skill_instructions}

SAFETY GUARDRAIL: Before submitting the final output, verify that no placeholder 
words like 'CONFIDENTIAL' or 'INTERNAL ONLY' are left in the text. If any sensitive data 
or names are missing, use '[Redacted]' instead. Do not hallucinate external details.
"""

print("🚀 Running your Capstone Agent via Gemini...")

# 5. Execute the generative model agent call
print(f"📊 Processing transcript ({len(transcript)} characters)...")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        f"TRANSCRIPT TO ANALYZE:\n{transcript}\n\nTASK: Apply your skills to the transcript above now"
    ],
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.1, # Keep temperature low for precise extraction
    )
)


# 6. Output the finalized markdown text straight to your terminal window
print("\n--- AGENT OUTPUT ---")
print(response.text)
