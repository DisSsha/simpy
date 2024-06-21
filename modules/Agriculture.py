import random

from models.module import Module


class Agriculture(Module):
    def __init__(self, state):
        super().__init__(state)
        self.output = 200

    def simulate_round(self):
        self.output += random.uniform(-50, 50)
        self.state.total_wealth += self.output  # Agriculture contributes to GDP
