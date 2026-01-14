import sys
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# 1. 현재 파일(test_langchain.py)의 부모의 부모인 프로젝트 루트를 찾음
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
src_dir = project_root / "src"

# 2. 'src' 폴더를 파이썬 경로에 추가 (이게 핵심입니다!)
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

# 3. 이제 'src.' 없이 'reviewer'로 시작하는 임포트가 가능해집니다.
try:
    from reviewer.langchain_reviewer import review_code_with_langchain
    print("✅ 모듈 임포트 성공!")
except ImportError as e:
    print(f"❌ 임포트 실패: {e}")
    print(f"현재 sys.path: {sys.path}")
    sys.exit(1)

def run_test():
    test_code = "def hello(): print('world')"
    print("--- 🚀 LangChain CLI 테스트 시작 ---")
    try:
        result = review_code_with_langchain(test_code)
        print(f"AI 응답:\n{result}")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    run_test()