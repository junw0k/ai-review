import os
# import sys
# from pathlib import Path

# 현재 파일(main.py) 위치를 기준으로 'src' 폴더 경로를 계산하여 추가
# current_dir = Path(__file__).resolve().parent
# src_dir = str(current_dir.parent)

# if src_dir not in sys.path:
#     sys.path.insert(0, src_dir)


from reviewer.github_client import get_pr_diff, post_comment
# from reviewer.ai_reviewer import review_code
from reviewer.langchain_reviewer import review_code_with_langchain

# def main():
#     # GitHub Actions에서 주입해주는 환경변수
#     repo_name = os.getenv("REPO_NAME")
#     pr_number = os.getenv("PR_NUMBER")
    
#     print(f" Repository: {repo_name}")
#     print(f" PR Number: {pr_number}")
    
#     if not repo_name or not pr_number:
#         print(" Error: REPO_NAME or PR_NUMBER not set")
#         print("   Make sure environment variables are configured in Workflow")
#         return
    
#     try:
#         pr_number = int(pr_number)
#     except ValueError:
#         print(f"Error: PR_NUMBER '{pr_number}' is not a valid number")
#         return
    
#     print(f"\nFetching PR #{pr_number} from {repo_name}...")
#     try:
#         diff = get_pr_diff(repo_name, pr_number)
        
#         print("Reviewing code with AI...")
#         review = review_code(diff)
        
#         print("Posting comment to PR...")
#         post_comment(repo_name, pr_number, review)
        
#         print("Done! AI review posted successfully.")
#     except Exception as e:
#         print(f"An error occurred during the review process: {e}")

def main():
    repo_name = os.getenv("REPO_NAME")
    pr_number = os.getenv("PR_NUMBER")
    
    print(f" Repository: {repo_name}")
    print(f" PR Number: {pr_number}")
    
    if not repo_name or not pr_number:
        print(" Error: REPO_NAME or PR_NUMBER not set")
        return
    
    try:
        pr_number = int(pr_number)
    except ValueError:
        print(f"Error: PR_NUMBER '{pr_number}' is not a valid number")
        return
    
    print(f"\nFetching PR #{pr_number} from {repo_name}...")
    try:
        diff = get_pr_diff(repo_name, pr_number)
        
        print("Reviewing code with AI (LangChain)...")
        
        # 2. 여기서 호출하는 함수를 변경합니다.
        review = review_code_with_langchain(diff)
        
        print("Posting comment to PR...")
        post_comment(repo_name, pr_number, review)
        
        print("Done! AI review posted successfully.")
    except Exception as e:
        print(f"An error occurred during the review process: {e}")


if __name__ == "__main__":
    main()