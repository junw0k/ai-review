import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 테스트용 코드 diff (실제론 GitHub에서 가져옴)
test_diff = """
def calculate_sum(a, b):
    result = a + b
    print(result)
    return result
"""

def review_code(code):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 저렴한 모델로 테스트
        messages=[
            {"role": "system", "content": "You are a code reviewer."},
            {"role": "user", "content": f"Review this code:\n{code}"}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("🤖 AI Code Review Starting...\n")
    review = review_code(test_diff)
    print(review)