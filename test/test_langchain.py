import os
import sys
from pathlib import Path
from unittest import TestCase, mock

# src 경로 추가
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from reviewer import langchain_reviewer  # noqa: E402


class LangChainReviewerTest(TestCase):
    def setUp(self) -> None:
        self._original_key = os.environ.get("GOOGLE_API_KEY")
        os.environ["GOOGLE_API_KEY"] = "dummy-key"

    def tearDown(self) -> None:
        if self._original_key is None:
            os.environ.pop("GOOGLE_API_KEY", None)
        else:
            os.environ["GOOGLE_API_KEY"] = self._original_key

    def test_review_code_with_langchain_invokes_chain(self):
        fake_chain = mock.Mock()
        fake_chain.invoke.return_value = " 결과 "
        with mock.patch.object(
            langchain_reviewer, "_build_chain", return_value=fake_chain
        ):
            output = langchain_reviewer.review_code_with_langchain("diff")

        fake_chain.invoke.assert_called_once_with({"code": "diff"})
        self.assertEqual(output, "결과")

    def test_review_code_with_langchain_requires_api_key(self):
        os.environ.pop("GOOGLE_API_KEY", None)
        with self.assertRaises(RuntimeError):
            langchain_reviewer.review_code_with_langchain("diff")
