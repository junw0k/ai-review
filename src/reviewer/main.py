import os
from dotenv import load_dotenv
from .github_client import get_pr_diff, post_comment
from .ai_reviewer import review_code

load_dotenv()

def main():
    repo_name = "junw0k/test_review"  # 실제 저장소로 변경
    pr_number = 1  # 실제 PR 번호로 변경
    
    print("Fetching PR...")
    diff = get_pr_diff(repo_name, pr_number)
    
    print("Reviewing...")
    review = review_code(diff)
    
    print("Posting...")
    post_comment(repo_name, pr_number, review)
    
    print("✅ Done!")

if __name__ == "__main__":
    main()