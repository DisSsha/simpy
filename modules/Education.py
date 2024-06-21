import random

from models.module import Module


class Education(Module):
    def __init__(self, state):
        super().__init__(state)

    def simulate_round(self):
        for c in self.state.citizens:
            c.education += random.uniform(0, 0.1)  # Simulate education improvements
