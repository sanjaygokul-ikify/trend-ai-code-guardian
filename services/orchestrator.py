from typing import List
from packages.core import CodeArtifact, SecurityScoreEngine, PatternDatabase
from packages.utils.logging import LoggingMixin

class Orchestrator(LoggingMixin):
    def __init__(self) -> None:
        super().__init__('Orchestrator')
        self.security_score_engine = SecurityScoreEngine({})
        self.pattern_database = PatternDatabase()

    def calculate_security_score(self, artifact: CodeArtifact) -> SecurityScore:
        security_score = self.security_score_engine.calculate_security_score(artifact)
        self.log_info(f'Security score for {artifact.code_hash}: {security_score.score}')
        return security_score

    def add_pattern(self, pattern: str, artifacts: List[str]) -> None:
        self.pattern_database.add_pattern(pattern, artifacts)
        self.log_info(f'Added pattern: {pattern}')