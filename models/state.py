from models.module import Module


class State:
    def __init__(self, system, citizens):
        self.system = system
        self.citizens = citizens
        self.modules = {}
        self.total_wealth = 0
        self.history = {
            "average_wealth": [],
            "inequality": [],
            "population": [],
            "total_wealth": [],
            "idh": [],
            "unemployment_rate": [],
        }

    def add_module(self, name, module):
        if isinstance(module, Module):
            self.modules[name] = module
        else:
            raise TypeError("Module must inherit from the Module base class")

    def simulate_round(self):
        for module in self.modules.values():
            module.simulate_round()
        self.collect_data()

    def collect_data(self):
        avg_wealth = self.average_wealth()
        inequality = self.inequality()
        population = len(self.citizens)
        self.history["average_wealth"].append(avg_wealth)
        self.history["inequality"].append(inequality)
        self.history["population"].append(population)
        self.history["total_wealth"].append(self.total_wealth)

    def average_wealth(self):
        return sum(c.wealth for c in self.citizens) / len(self.citizens)

    def inequality(self):
        wealths = [c.wealth for c in self.citizens]
        return max(wealths) - min(wealths)
        return max(wealths) - min(wealths)
