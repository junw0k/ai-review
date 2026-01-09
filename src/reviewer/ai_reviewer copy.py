import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def review_code(code: str) -> str:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"You are a code reviewer. Review this code:\n{code}"
    )
    return response.text