import argparse
import sys
from services.orchestrator import Orchestrator
from packages.core import CodeArtifact

def main() -> None:
    parser = argparse.ArgumentParser(description='Autonomous Anomaly Detection System')
    parser.add_argument('--code-hash', type=str, required=True)
    parser.add_argument('--imports', type=str, nargs='+', required=True)
    args = parser.parse_args()

    orchestrator = Orchestrator()
    artifact = CodeArtifact(args.code_hash, args.imports)
    security_score = orchestrator.calculate_security_score(artifact)
    print(f'Security score: {security_score.score}')

if __name__ == '__main__':
    main()