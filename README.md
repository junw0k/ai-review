
# AI Code Reviewer

GitHub Pull Request 변경 사항을 Google Gemini 모델로 자동 리뷰하는 실험용 프로젝트입니다. 기본 SDK 경로와 LangChain 기반 경로를 모두 지원하여 필요에 따라 선택적으로 사용할 수 있습니다.

## 환경 변수

| 변수 | 설명 |
| --- | --- |
| `GITHUB_TOKEN` | PR diff 조회/코멘트 작성을 위한 GitHub Personal Access Token |
| `REPO_NAME` | `<owner>/<repo>` 형식의 저장소 이름 |
| `PR_NUMBER` | 리뷰 대상 PR 번호 |
| `GOOGLE_API_KEY` | Gemini API 키 |
| `REVIEW_BACKEND` | `sdk`(기본) 또는 `langchain` 중 선택 |
| `GOOGLE_MODEL` | 사용할 Gemini 모델 이름 (기본 `gemini-3-flash-preview`) |
| `GOOGLE_TEMPERATURE` | LangChain 경로에서 사용할 온도 값 (기본 `0.1`) |

## 실행

```bash
export REPO_NAME="owner/repo"
export PR_NUMBER="123"
export GITHUB_TOKEN="ghp_..."
export GOOGLE_API_KEY="AIza..."

# 기본 SDK
python -m reviewer.main

# LangChain 체인을 사용하고 싶다면
REVIEW_BACKEND=langchain python -m reviewer.main
```

## 테스트

LangChain 경로를 모의 객체로 검증하는 단위 테스트가 포함되어 있습니다. `GOOGLE_API_KEY`가 없어도 실행되도록 구성되어 있으므로 다음 명령으로 확인할 수 있습니다.

```bash
python -m unittest test.test_langchain
```
