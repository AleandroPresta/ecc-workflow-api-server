from .InequalitiesStrategy import InequalitiesStrategy

class WorkflowServiceOptimizerFacade:
    
    inqeualities_strategy: InequalitiesStrategy
    
    def __init__(self, VERBOSE: bool, distance_function=None):
        self.inqeualities_strategy = InequalitiesStrategy(distance_function=distance_function, VERBOSE=VERBOSE)
        
    
    def findOptimalServices(self, workflow: dict, catalog: dict, solver_type: str = "inequalities"):
        if solver_type == "inequalities":
            return 1 # self.inqeualities_strategy.solve(workflow, catalog) TODO add connection between facade and strategy
        else:
            raise ValueError("Invalid solver type")