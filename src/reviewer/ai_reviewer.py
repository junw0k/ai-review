import os
from google import genai


client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def review_code(code: str) -> str:
    prompt = (
        "당신은 숙련된 파이썬 개발자이자 코드 리뷰어입니다.\n"
        "다음 코드 변경 사항(diff)을 분석하고 리뷰를 작성하라:\n\n"
        f"{code}\n\n"
        "리뷰 지침:\n"
        "1. 중요한 버그나 잠재적인 오류가 있다면 지적하라.\n"
        "2. 가독성과 유지보수성을 높일 수 있는 개선 방안을 제안하라.\n"
        "3. 모든 답변은 한국어로 작성해 해라.\n"
        
    )
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text