from models.module import Module


class IDH(Module):
    def __init__(self, state):
        super().__init__(state)
        self.health_index = 0
        self.education_index = 0
        self.income_index = 0

    def calculate_health_index(self):
        # Calculate based on healthcare module data
        self.health_index = min(
            1.0,
            sum(c.health for c in self.state.citizens) / len(self.state.citizens) / 100,
        )

    def calculate_education_index(self):
        # Calculate based on education module data
        self.education_index = min(
            1.0,
            sum(c.education for c in self.state.citizens)
            / len(self.state.citizens)
            / 10,
        )

    def calculate_income_index(self):
        # Calculate based on average wealth
        avg_income = sum(c.wealth for c in self.state.citizens) / len(
            self.state.citizens
        )
        self.income_index = min(1.0, avg_income / 100000)

    def simulate_round(self):
        self.calculate_health_index()
        self.calculate_education_index()
        self.calculate_income_index()
        idh = (self.health_index + self.education_index + self.income_index) / 3
        self.state.history["idh"].append(idh)
        self.state.history["idh"].append(idh)
