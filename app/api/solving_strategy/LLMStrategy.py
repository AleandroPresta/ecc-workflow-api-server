from .gptsolver import solver

class LLMStrategy ():
    def __init__(self):
        pass
    
    def solve(self, workflow: dict, catalog: dict) -> dict:
        return {
            'message': 'Workflow and catalog successfully received',
            'result': solver.solve(workflow, catalog)
        }