from github import Github
import os

def get_pr_diff(repo_name: str, pr_number: int) -> str:
    """PR의 코드 변경사항 가져오기"""
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    diff = ""
    for file in pr.get_files():
        diff += f"\n### {file.filename}\n"
        diff += file.patch or ""
    
    return diff

def post_comment(repo_name: str, pr_number: int, comment: str):
    """PR에 코멘트 작성"""
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    pr.create_issue_comment(f"## 🤖 AI Code Review\n\n{comment}")