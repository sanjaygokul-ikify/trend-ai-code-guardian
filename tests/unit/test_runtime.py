import unittest
from services.orchestrator import Orchestrator

class TestOrchestrator(unittest.TestCase):
    def test_calculate_security_score(self) -> None:
        orchestrator = Orchestrator()
        artifact = CodeArtifact('code_hash', ['import1', 'import2'])
        security_score = orchestrator.calculate_security_score(artifact)
        self.assertIsNotNone(security_score)
