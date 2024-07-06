from abc import ABC, abstractmethod

class SolvingStrategy(ABC):
    @abstractmethod
    def solve(self, workflow, catalog):
        pass