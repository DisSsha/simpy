import random
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt


class Citizen:
    def __init__(self, id, age=0, wealth=0, productivity=0):
        self.id = id
        self.age = age
        self.wealth = wealth
        self.productivity = productivity

    def age_one_year(self):
        self.age += 1


class Module(ABC):
    def __init__(self, state):
        self.state = state

    @abstractmethod
    def simulate_round(self):
        pass


class Economy(Module):
    def __init__(self, state):
        super().__init__(state)

    def distribute_resources(self):
        if self.state.system == "communism":
            total_wealth = sum(c.wealth for c in self.state.citizens)
            equal_share = total_wealth / len(self.state.citizens)
            for c in self.state.citizens:
                c.wealth = equal_share
        elif self.state.system == "capitalism":
            for c in self.state.citizens:
                c.wealth += random.randint(0, 100)

    def simulate_round(self):
        self.distribute_resources()


class Healthcare(Module):
    def __init__(self, state):
        super().__init__(state)
        self.quality = 1.0
        self.pandemic = False
        self.pandemic_impact = 0.1

    def handle_healthcare(self):
        if random.random() < 0.05:  # 5% chance of pandemic each round
            self.pandemic = True
        if self.pandemic:
            for c in self.state.citizens[
                :
            ]:  # Copy the list to avoid modification during iteration
                if random.random() < self.pandemic_impact:
                    self.state.citizens.remove(c)
            self.pandemic = False  # Assume the pandemic is handled within one round

    def simulate_round(self):
        self.handle_healthcare()


class Population(Module):
    def __init__(self, state):
        super().__init__(state)

    def age_population(self):
        for c in self.state.citizens:
            c.age_one_year()

    def adjust_population(self):
        # Remove old citizens
        self.state.citizens = [c for c in self.state.citizens if c.age < 80]
        # Add new citizens
        birth_rate = 0.02  # 2% birth rate
        num_new_citizens = int(len(self.state.citizens) * birth_rate)
        new_citizens = [
            Citizen(id=len(self.state.citizens) + i) for i in range(num_new_citizens)
        ]
        self.state.citizens.extend(new_citizens)

    def simulate_round(self):
        self.age_population()
        self.adjust_population()


class State:
    def __init__(self, system, citizens):
        self.system = system
        self.citizens = citizens
        self.modules = {}
        self.history = {"average_wealth": [], "inequality": [], "population": []}

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

    def average_wealth(self):
        return sum(c.wealth for c in self.citizens) / len(self.citizens)

    def inequality(self):
        wealths = [c.wealth for c in self.citizens]
        return max(wealths) - min(wealths)


def simulate_states(rounds, initial_population, systems):
    states = []

    for system in systems:
        citizens = [Citizen(id=i) for i in range(initial_population)]
        state = State(system=system, citizens=citizens)

        economy = Economy(state)
        healthcare = Healthcare(state)
        population = Population(state)

        state.add_module("economy", economy)
        state.add_module("healthcare", healthcare)
        state.add_module("population", population)

        states.append(state)

    for _ in range(rounds):
        for state in states:
            state.simulate_round()

    return states


# Simulation parameters
rounds = 50
initial_population = 100
systems = ["capitalism", "communism"]

# Run the simulation
states = simulate_states(rounds, initial_population, systems)

# Plotting the results
plt.figure(figsize=(18, 12))

# Average Wealth Plot
plt.subplot(2, 3, 1)
for state in states:
    plt.plot(state.history["average_wealth"], label=f"Average Wealth ({state.system})")
plt.xlabel("Rounds")
plt.ylabel("Average Wealth")
plt.title("Average Wealth Over Time")
plt.legend()

# Inequality Plot
plt.subplot(2, 3, 2)
for state in states:
    plt.plot(state.history["inequality"], label=f"Inequality ({state.system})")
plt.xlabel("Rounds")
plt.ylabel("Inequality")
plt.title("Inequality Over Time")
plt.legend()

# Population Plot
plt.subplot(2, 3, 3)
for state in states:
    plt.plot(state.history["population"], label=f"Population ({state.system})")
plt.xlabel("Rounds")
plt.ylabel("Population")
plt.title("Population Over Time")
plt.legend()

plt.tight_layout()
plt.show()
