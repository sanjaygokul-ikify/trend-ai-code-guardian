from dataclasses import dataclass
from typing import List


@dataclass
class CodeArtifact:
    code_hash: str
    imports: List[str]


@dataclass
class SecurityScore:
    score: float