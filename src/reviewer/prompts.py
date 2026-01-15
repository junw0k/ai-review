"""공통 코드 리뷰 프롬프트 정의."""

SYSTEM_PROMPT = "당신은 숙련된 코드 리뷰어입니다. 모든 답변은 한국어로 작성하세요."

HUMAN_PROMPT_TEMPLATE = (
    "다음 코드 변경 사항(diff)을 분석하고 리뷰를 작성하라:\n\n"
    "{code}\n\n"
    "리뷰 지침:\n"
    "1. 중요한 버그나 잠재적인 오류가 있다면 지적하라.\n"
    "2. 가독성과 유지보수성을 높일 수 있는 개선 방안을 제안하라.\n"
    "3. 필요한 경우 테스트나 문서화 보완을 권장하라."
)


def build_sdk_prompt(diff: str) -> str:
    """단일 문자열 프롬프트 생성."""
    return f"{SYSTEM_PROMPT}\n\n{HUMAN_PROMPT_TEMPLATE.format(code=diff)}"
