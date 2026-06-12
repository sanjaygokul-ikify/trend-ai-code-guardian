import unittest
from cli.main import main
from packages.core import CodeArtifact
from unittest.mock import patch

class TestPipeline(unittest.TestCase):
    @patch('sys.argv', ['main.py', '--code-hash', 'code_hash', '--imports', 'import1', 'import2'])
    def test_main(self) -> None:
        main()
