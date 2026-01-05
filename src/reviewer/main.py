import os
from google import genai # 새로운 라이브러리 사용
from dotenv import load_dotenv

load_dotenv()

# 클라이언트 설정
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

test_diff = """
def calculate_sum(a, b):
    result = a + b
    print(result)
    return result
"""

def review_code(code):
    # 최신 SDK 방식: models.generate
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=f"You are a professional code reviewer. Review this code:\n{code}"
    )
    return response.text

if __name__ == "__main__":
    print("🤖 AI Code Review (Gemini New SDK) Starting...\n")
    try:
        review = review_code(test_diff)
        print(review)
    except Exception as e:
        print(f"❌ Error occurred: {e}")