import random

from models.module import Module


class Trade(Module):
    def __init__(self, state):
        super().__init__(state)
        self.exports = 500
        self.imports = 400
        self.competitiveness = 0.5

    def simulate_round(self):
        # Simulate changes in trade balance with competitiveness
        self.exports += self.competitiveness * random.uniform(-50, 50)
        self.imports += (1 - self.competitiveness) * random.uniform(-50, 50)

        trade_balance = self.exports - self.imports
        self.state.total_wealth += trade_balance
        self.state.trade_balance = trade_balance
        self.state.total_wealth += trade_balance
        self.state.trade_balance = trade_balance
        self.state.total_wealth += trade_balance
        self.state.trade_balance = trade_balance
