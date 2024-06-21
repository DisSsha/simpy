import random

from models.module import Module


class LaborMarket(Module):
    def __init__(self, state):
        super().__init__(state)
        self.unemployment_rate = 0.1  # Starting unemployment rate

    def simulate_round(self):
        for c in self.state.citizens:
            if self.state.system == "communism":
                c.employed = True
            else:
                if random.random() < self.unemployment_rate:
                    c.employed = False
                else:
                    c.employed = True

        employed_count = sum(1 for c in self.state.citizens if c.employed)
        self.unemployment_rate = 1 - (employed_count / len(self.state.citizens))
        self.state.history["unemployment_rate"].append(self.unemployment_rate)
