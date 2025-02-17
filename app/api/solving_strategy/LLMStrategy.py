from .SolvingStrategy import SolvingStrategy
from .gptsolver import solver

class LLMStrategy (SolvingStrategy):
    def solve(self, workflow: dict, catalog: dict) -> dict:
        return {
            'message': 'Workflow and catalog successfully received',
            'result': solver.solve(workflow, catalog)
        }