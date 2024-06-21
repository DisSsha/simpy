import random

from models.module import Module


class GDP(Module):
    def __init__(self, state):
        super().__init__(state)
        self.gdp = 10000

    def simulate_round(self):
        # Calculate growth rate based on some economic factors
        base_growth_rate = 0.02  # Base growth rate of 2%
        productivity_growth = (
            sum(c.wealth for c in self.state.citizens) / len(self.state.citizens) * 0.01
        )
        investment_growth = random.uniform(0.01, 0.03)  # Simulating investments
        random_fluctuation = random.uniform(-0.01, 0.01)  # Random economic fluctuation

        growth_rate = (
            base_growth_rate
            + productivity_growth
            + investment_growth
            + random_fluctuation
        )

        # Simulate economic growth
        growth = self.gdp * growth_rate
        self.gdp += growth
        # Pass the new GDP to the state's economy
        self.state.total_wealth = self.gdp
