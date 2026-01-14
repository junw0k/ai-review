import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def review_code_with_langchain(code: str) -> str:
    # 1. 모델 설정 (온도를 낮춰 일관된 리뷰 유도)
    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0.1
    )

    # 2. 프롬프트 템플릿 정의
    prompt = ChatPromptTemplate.from_messages([
        ("system", "당신은 숙련된 코드 리뷰어입니다. 한국어로 친절하고 전문적으로 답변하세요."),
        ("human", "다음 코드의 변경 사항을 리뷰하고 개선점을 제안해 주세요:\n\n{code}")
    ])

    # 3. 체인(Chain) 구성: 프롬프트 -> 모델 -> 출력 파서
    chain = prompt | llm | StrOutputParser()

    # 4. 실행 및 결과 반환
    return chain.invoke({"code": code})