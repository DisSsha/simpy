from abc import ABC, abstractmethod


class Module(ABC):
    def __init__(self, state):
        self.state = state

    @abstractmethod
    def simulate_round(self):
        pass
        pass
