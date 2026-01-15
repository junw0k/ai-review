import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from reviewer.prompts import HUMAN_PROMPT_TEMPLATE, SYSTEM_PROMPT


def _build_chain() -> ChatPromptTemplate:
    """LangChain 체인을 구성해 재사용."""
    model_name = os.getenv("GOOGLE_MODEL", "gemini-3-flash-preview")
    temperature = float(os.getenv("GOOGLE_TEMPERATURE", "0.1"))
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature,
    )
    prompt = ChatPromptTemplate.from_messages(
        [("system", SYSTEM_PROMPT), ("human", HUMAN_PROMPT_TEMPLATE)]
    )
    return prompt | llm | StrOutputParser()


def review_code_with_langchain(code_diff: str) -> str:
    """LangChain 기반 코드 리뷰."""
    if not os.getenv("GOOGLE_API_KEY"):
        raise RuntimeError("GOOGLE_API_KEY 환경변수가 설정되지 않았습니다.")
    chain = _build_chain()
    return chain.invoke({"code": code_diff}).strip()
