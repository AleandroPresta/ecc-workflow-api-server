from abc import ABC, abstractmethod

class SolvingStrategy(ABC):
    @abstractmethod
    def solve(self, workflow: dict, catalog: dict) -> dict:
        pass