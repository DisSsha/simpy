import random

from models.module import Module


class Economy(Module):
    def __init__(self, state):
        super().__init__(state)

    def distribute_resources(self):
        total_wealth = self.state.total_wealth
        if self.state.system == "communism":
            equal_share = total_wealth / len(self.state.citizens)
            for c in self.state.citizens:
                c.wealth += equal_share
        elif self.state.system == "capitalism":
            productivity_factor = [
                random.uniform(0.5, 1.5) for _ in self.state.citizens
            ]
            total_productivity = sum(productivity_factor)
            for c, factor in zip(self.state.citizens, productivity_factor):
                c.wealth += (factor / total_productivity) * total_wealth

    def simulate_round(self):
        self.distribute_resources()
