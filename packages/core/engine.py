import logging
from collections import defaultdict
from typing import Dict, List
from .types import CodeArtifact, SecurityScore
from .exceptions import InvalidArtifactError, SecurityScoringError


class SecurityScoreEngine:
    def __init__(self, knowledge_graph:
        Dict[str, List[str]]) -> None:
        self.knowledge_graph = knowledge_graph
        self.logger = logging.getLogger(__name__)

    def calculate_security_score(self, artifact: CodeArtifact) -> SecurityScore:
        try:
            # Extract features from the artifact
            features = self._extract_features(artifact)
            # Calculate the security score based on the knowledge graph
            score = self._calculate_score(features, self.knowledge_graph)
            return score
        except InvalidArtifactError as e:
            self.logger.error(f"Invalid artifact: {e}")
            raise SecurityScoringError("Failed to calculate security score")
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            raise SecurityScoringError("Failed to calculate security score due to unexpected error")

    def _extract_features(self, artifact: CodeArtifact) -> List[str]:
        if artifact is None:
            raise InvalidArtifactError("Artifact cannot be None")
        # Implement feature extraction logic
        features: List[str] = []
        # For example:
        features.append(artifact.code_hash)
        features.extend(artifact.imports)  # handle imports as separate features
        return features

    def _calculate_score(self, features: List[str], knowledge_graph: Dict[str, List[str]]) -> SecurityScore:
        # Implement scoring logic
        score: float = 0.0
        # For example:
        for feature in features:
            if feature in knowledge_graph:
                score += 1.0
        # added a check to avoid division by zero
        if features:
            return SecurityScore(score / len(features))
        else:
            return SecurityScore(0.0)
        # Added a check to avoid None values
        if score is None:
            return SecurityScore(0.0)


class PatternDatabase:
    def __init__(self) -> None:
        self.patterns: Dict[str, List[str]] = defaultdict(list)
        self.logger = logging.getLogger(__name__)

    def add_pattern(self, pattern: str, artifacts: List[str]) -> None:
        self.patterns[pattern].extend(artifacts)
        self.logger.info(f"Added pattern: {pattern}")

    def get_patterns(self, artifact: str) -> List[str]:
        return self.patterns.get(artifact, [])