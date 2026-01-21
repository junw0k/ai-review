# src/reviewer/retrievers/reader.py
import os

class ConventionReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_all_conventions(self):
        """파일 전체 내용을 읽어 반환합니다."""
        if not os.path.exists(self.file_path):
            return "지정된 코딩 규칙 파일이 없습니다."
        
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()