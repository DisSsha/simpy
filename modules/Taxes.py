from models.module import Module


class Taxes(Module):
    def __init__(self, state, tax_rate=0.2):
        super().__init__(state)
        self.tax_rate = tax_rate

    def collect_taxes(self):
        total_taxes = 0
        for c in self.state.citizens:
            taxes = c.wealth * self.tax_rate
            c.wealth -= taxes
            total_taxes += taxes
        return total_taxes

    def simulate_round(self):
        total_taxes = self.collect_taxes()
        # Use collected taxes for public investment (increasing GDP)
        self.state.total_wealth += (
            total_taxes * 0.5
        )  # 50% of taxes are reinvested into the economy
