import os
from typing import Optional

from google import genai

from reviewer.prompts import build_sdk_prompt

_client: Optional[genai.Client] = None


def _get_client() -> genai.Client:
    """지연 초기화된 Gemini 클라이언트 반환."""
    global _client
    if _client is None:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise RuntimeError("GOOGLE_API_KEY 환경변수가 설정되지 않았습니다.")
        _client = genai.Client(api_key=api_key)
    return _client


def review_code(code_diff: str) -> str:
    """기본 Google SDK를 이용해 코드 리뷰를 생성."""
    prompt = build_sdk_prompt(code_diff)
    model_name = os.getenv("GOOGLE_MODEL", "gemini-3-flash-preview")
    response = _get_client().models.generate_content(
        model=model_name,
        contents=prompt,
    )
    text = getattr(response, "text", "").strip()
    if not text:
        raise RuntimeError("Gemini 응답에 텍스트가 포함되지 않았습니다.")
    return text


## 
from reviewer.retrievers.reader import ConventionReader
from reviewer.prompts import REVIEW_P_TEMPLATE

def run_review(diff_content):
    # 1. 규칙 읽기 (무거운 검색 로직 제거)
    reader = ConventionReader("src/reviewer/config/conventions.md")
    conventions = reader.get_all_conventions()
    
    # 2. 프롬프트 생성
    prompt_text = REVIEW_P_TEMPLATE.format(
        conventions=conventions, 
        diff=diff_content
    )