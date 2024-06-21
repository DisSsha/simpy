class Citizen:
    def __init__(self, id, age=0, wealth=0, education=0, health=100, employed=False):
        self.id = id
        self.age = age
        self.wealth = wealth
        self.education = education
        self.health = health
        self.employed = employed

    def age_one_year(self):
        self.age += 1
