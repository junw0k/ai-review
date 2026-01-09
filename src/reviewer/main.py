import os
from dotenv import load_dotenv

# 상대 경로(.) 대신 패키지명을 포함한 절대 경로를 사용합니다.
# 이 방식은 PYTHONPATH가 설정된 환경에서 가장 안전합니다.
from reviewer.github_client import get_pr_diff, post_comment
from reviewer.ai_reviewer import review_code

load_dotenv()

def main():
    # GitHub Actions에서 주입해주는 환경변수
    repo_name = os.getenv("REPO_NAME")
    pr_number = os.getenv("PR_NUMBER")
    
    print(f" Repository: {repo_name}")
    print(f" PR Number: {pr_number}")
    
    if not repo_name or not pr_number:
        print(" Error: REPO_NAME or PR_NUMBER not set")
        print("   Make sure environment variables are configured in Workflow")
        return
    
    try:
        pr_number = int(pr_number)
    except ValueError:
        print(f"Error: PR_NUMBER '{pr_number}' is not a valid number")
        return
    
    print(f"\nFetching PR #{pr_number} from {repo_name}...")
    try:
        diff = get_pr_diff(repo_name, pr_number)
        
        print("Reviewing code with AI...")
        review = review_code(diff)
        
        print("Posting comment to PR...")
        post_comment(repo_name, pr_number, review)
        
        print("Done! AI review posted successfully.")
    except Exception as e:
        print(f"An error occurred during the review process: {e}")

if __name__ == "__main__":
    main()