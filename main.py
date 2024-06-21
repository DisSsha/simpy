import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from models import Citizen, State
from models.module import Module
from modules.Agriculture import Agriculture
from modules.Economy import Economy
from modules.Education import Education
from modules.Environment import Environment
from modules.GDP import GDP
from modules.Healthcare import Healthcare
from modules.IDH import IDH
from modules.Industry import Industry
from modules.Infrastructure import Infrastructure
from modules.Innovation import Innovation
from modules.LaborMarket import LaborMarket
from modules.Population import Population
from modules.Services import Services
from modules.SocialSecurity import SocialSecurity
from modules.Taxes import Taxes
from modules.Trade import Trade


def simulate_states(rounds, initial_population, systems):
    states = []
    results = []

    for system in systems:
        citizens = [Citizen(id=i) for i in range(initial_population)]
        state = State(system=system, citizens=citizens)

        modules = [
            GDP(state),
            Economy(state),
            Healthcare(state),
            Population(state),
            Trade(state),
            Taxes(state),
            Industry(state),
            Agriculture(state),
            Education(state),
            IDH(state),
            LaborMarket(state),
            Services(state),
            Infrastructure(state),
            Innovation(state),
            Environment(state),
            SocialSecurity(state),
        ]

        for module in modules:
            state.add_module(module.__class__.__name__.lower(), module)

        states.append(state)

    for _ in range(rounds):
        for state in states:
            state.simulate_round()

    for state in states:
        for i in range(rounds):
            results.append(
                {
                    "system": state.system,
                    "round": i,
                    "average_wealth": state.history["average_wealth"][i],
                    "inequality": state.history["inequality"][i],
                    "population": state.history["population"][i],
                    "total_wealth": state.history["total_wealth"][i],
                    "idh": state.history["idh"][i],
                    "unemployment_rate": state.history["unemployment_rate"][i],
                }
            )

    return pd.DataFrame(results)


# Simulation parameters
rounds = 100
initial_population = 100
systems = ["capitalism", "communism"]

# Run the simulation and store results in a DataFrame
results_df = simulate_states(rounds, initial_population, systems)

# Save results to CSV
results_df.to_csv("simulation_results.csv", index=False)

# Display a sample of the data
print(results_df.head())

# Visualization of results including IDH
sns.set(style="darkgrid")

fig, axes = plt.subplots(5, 1, figsize=(12, 30))

sns.lineplot(ax=axes[0], data=results_df, x="round", y="average_wealth", hue="system")
axes[0].set_title("Average Wealth Over Time")
axes[0].set_xlabel("Rounds")
axes[0].set_ylabel("Average Wealth")

sns.lineplot(ax=axes[1], data=results_df, x="round", y="inequality", hue="system")
axes[1].set_title("Inequality Over Time")
axes[1].set_xlabel("Rounds")
axes[1].set_ylabel("Inequality")

sns.lineplot(ax=axes[2], data=results_df, x="round", y="population", hue="system")
axes[2].set_title("Population Over Time")
axes[2].set_xlabel("Rounds")
axes[2].set_ylabel("Population")

sns.lineplot(ax=axes[3], data=results_df, x="round", y="total_wealth", hue="system")
axes[3].set_title("Total Wealth Over Time")
axes[3].set_xlabel("Rounds")
axes[3].set_ylabel("Total Wealth")

sns.lineplot(ax=axes[4], data=results_df, x="round", y="idh", hue="system")
axes[4].set_title("Human Development Index Over Time")
axes[4].set_xlabel("Rounds")
axes[4].set_ylabel("Human Development Index")

plt.tight_layout()
plt.show()
