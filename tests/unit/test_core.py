import unittest
from packages.core import SecurityScoreEngine, CodeArtifact, SecurityScore
from packages.core.exceptions import InvalidArtifactError, SecurityScoringError

class TestSecurityScoreEngine(unittest.TestCase):
    def test_calculate_security_score(self) -> None:
        knowledge_graph = {'feature1': ['import1', 'import2']}
        security_score_engine = SecurityScoreEngine(knowledge_graph)
        artifact = CodeArtifact('code_hash', ['import1', 'import2'])
        security_score = security_score_engine.calculate_security_score(artifact)
        self.assertIsNotNone(security_score)
        self.assertIsInstance(security_score, SecurityScore)

    def test_calculate_security_score_invalid_artifact(self) -> None:
        security_score_engine = SecurityScoreEngine({})
        with self.assertRaises(SecurityScoringError):
            security_score_engine.calculate_security_score(None)
