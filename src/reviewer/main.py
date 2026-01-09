import os
from dotenv import load_dotenv
from .github_client import get_pr_diff, post_comment
from .ai_reviewer import review_code

load_dotenv()

def main():
    # 환경변수 가져오기
    repo_name = os.getenv("REPO_NAME")
    pr_number = os.getenv("PR_NUMBER")
    
    # 디버깅 출력
    print(f"🔍 Repository: {repo_name}")
    print(f"🔍 PR Number: {pr_number}")
    
    # 환경변수 검증
    if not repo_name or not pr_number:
        print("❌ Error: REPO_NAME or PR_NUMBER not set")
        print("   Make sure environment variables are configured")
        return
    
    # PR 번호 변환 (에러 처리)
    try:
        pr_number = int(pr_number)
    except ValueError:
        print(f"❌ Error: PR_NUMBER '{pr_number}' is not a valid number")
        return
    
    print(f"\n📥 Fetching PR #{pr_number} from {repo_name}...")
    diff = get_pr_diff(repo_name, pr_number)
    
    print("🤖 Reviewing code with AI...")
    review = review_code(diff)
    
    print("💬 Posting comment to PR...")
    post_comment(repo_name, pr_number, review)
    
    print("✅ Done! AI review posted successfully.")

if __name__ == "__main__":
    main()