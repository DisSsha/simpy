import random

from models.module import Module


class Services(Module):
    def __init__(self, state):
        super().__init__(state)
        self.output = 2000  # Initial output from services sector

    def simulate_round(self):
        # Simulate changes in services output
        self.output += random.uniform(-200, 200)
        # Services contribute to GDP
        self.state.total_wealth += self.output * 0.2
        self.output += random.uniform(-200, 200)
        # Services contribute to GDP
        self.state.total_wealth += self.output * 0.2
