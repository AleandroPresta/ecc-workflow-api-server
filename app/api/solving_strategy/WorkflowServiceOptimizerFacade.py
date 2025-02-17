class WorkflowServiceOptimizerFacade:
    
    def __init__(self):
        pass
        
    
    def findOptimalServices(self, workflow: dict, catalog: dict, solver_type: str = "inequalities"):
        if solver_type == "inequalities":
            raise Exception("Not implemented yet")
        if solver_type == "llm":
            return 2
        else:
            raise ValueError("Invalid solver type")