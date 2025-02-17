from SolvingStrategy import SolvingStrategy

class LlmStrategy (SolvingStrategy):
    def solve(self, workflow: dict, catalog: dict) -> dict:
        return {
            'message': 'Workflow and catalog successfully received',
            'result': 'llm'
        }