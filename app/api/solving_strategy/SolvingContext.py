from SolvingStrategy import SolvingStrategy

class SolvingContext:
    def __init__(self, strategy: SolvingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SolvingStrategy):
        self.strategy = strategy

    def solve(self, workflow, catalog):
        return self.strategy.solve(workflow, catalog)