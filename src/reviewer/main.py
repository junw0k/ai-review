import os
from typing import Callable, Dict

from reviewer.ai_reviewer import review_code
from reviewer.github_client import get_pr_diff, post_comment
from reviewer.langchain_reviewer import review_code_with_langchain

REVIEWERS: Dict[str, Callable[[str], str]] = {
    "sdk": review_code,
    "langchain": review_code_with_langchain,
}


def _resolve_reviewer() -> Callable[[str], str]:
    backend = os.getenv("REVIEW_BACKEND", "sdk").lower()
    if backend not in REVIEWERS:
        valid = ", ".join(REVIEWERS.keys())
        raise ValueError(
            f"지원하지 않는 REVIEW_BACKEND '{backend}'. 사용할 수 있는 값: {valid}"
        )
    print(f"Using review backend: {backend}")
    return REVIEWERS[backend]


def _validate_github_env() -> bool:
    if not os.getenv("GITHUB_TOKEN"):
        print(" Error: GITHUB_TOKEN not set")
        return False
    return True


def main():
    repo_name = os.getenv("REPO_NAME")
    pr_number = os.getenv("PR_NUMBER")

    print(f" Repository: {repo_name}")
    print(f" PR Number: {pr_number}")

    if not repo_name or not pr_number:
        print(" Error: REPO_NAME or PR_NUMBER not set")
        print("   Make sure environment variables are configured in Workflow")
        return

    if not _validate_github_env():
        return

    try:
        reviewer = _resolve_reviewer()
    except ValueError as err:
        print(f" Error: {err}")
        return

    try:
        pr_number_int = int(pr_number)
    except ValueError:
        print(f"Error: PR_NUMBER '{pr_number}' is not a valid number")
        return

    print(f"\nFetching PR #{pr_number_int} from {repo_name}...")
    try:
        diff = get_pr_diff(repo_name, pr_number_int)

        print("Reviewing code with AI...")
        review = reviewer(diff)

        print("Posting comment to PR...")
        post_comment(repo_name, pr_number_int, review)

        print("Done! AI review posted successfully.")
    except Exception as e:
        print(f"An error occurred during the review process: {e}")

# def main():
#     repo_name = os.getenv("REPO_NAME")
#     pr_number = os.getenv("PR_NUMBER")
    
#     print(f" Repository: {repo_name}")
#     print(f" PR Number: {pr_number}")
    
#     if not repo_name or not pr_number:
#         print(" Error: REPO_NAME or PR_NUMBER not set")
#         return
    
#     try:
#         pr_number = int(pr_number)
#     except ValueError:
#         print(f"Error: PR_NUMBER '{pr_number}' is not a valid number")
#         return
    
#     print(f"\nFetching PR #{pr_number} from {repo_name}...")
#     try:
#         diff = get_pr_diff(repo_name, pr_number)
        
#         print("Reviewing code with AI (LangChain)...")
        
#         # 2. 여기서 호출하는 함수를 변경합니다.
#         review = review_code_with_langchain(diff)
        
#         print("Posting comment to PR...")
#         post_comment(repo_name, pr_number, review)
        
#         print("Done! AI review posted successfully.")
#     except Exception as e:
#         print(f"An error occurred during the review process: {e}")


if __name__ == "__main__":
    main()
