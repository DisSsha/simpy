from models.module import Module


class Environment(Module):
    def __init__(self, state):
        super().__init__(state)

    def simulate_round(self):
        pass