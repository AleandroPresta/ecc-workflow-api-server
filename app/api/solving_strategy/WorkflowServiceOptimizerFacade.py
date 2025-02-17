from .LLMStrategy import LLMStrategy
from .SolvingStrategy import SolvingStrategy

class WorkflowServiceOptimizerFacade:
    
    def __init__(self):
        self.llm_strategy = LLMStrategy()
        
    
    def findOptimalServices(self, workflow: dict, catalog: dict, solver_type: str = "inequalities"):
        if solver_type == "inequalities":
            raise Exception("Not implemented yet")
        if solver_type == "llm":
            return self.llm_strategy.solve(workflow, catalog)
        else:
            raise ValueError("Invalid solver type")