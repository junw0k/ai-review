# 1. 파이썬 최신 슬림 이미지 사용
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. uv 설치 (사용자님의 기존 방식 유지)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvbin/uv
ENV PATH="/uvbin:${PATH}"

# 4. 의존성 파일 복사 및 설치
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache

# 5. 소스 코드 복사
COPY src/ ./src/

# 6. PYTHONPATH 설정 (모듈 경로 문제 해결)
ENV PYTHONPATH="/app/src"

# 7. 실행 명령 (main.py 호출)
# 주의: Docker 환경이므로 실행 경로를 정확히 지정합니다.
ENTRYPOINT ["uv", "--project", "/app", "run", "python", "/app/src/reviewer/main.py"]