# Base class: Character
class Character:
    def __init__(self, name, power_level):
        self._name = name  # Encapsulated with underscore
        self._power_level = power_level
    def show_stats(self):
        print(f"{self._name} has power level {self._power_level}.")
    def use_power(self):
        print(f"{self._name} uses their power!")
class Superhero(Character):
    def __init__(self, name, power_level, superpower):
        super().__init__(name, power_level)
        self.superpower = superpower
    def use_power(self):
        print(f"{self._name} uses {self.superpower}!")
class Villain(Character):
    def __init__(self, name, power_level, evil_plan):
        super().__init__(name, power_level)
        self.evil_plan = evil_plan

    def use_power(self):
        print(f"{self._name} executes evil plan: {self.evil_plan}!")
hero = Superhero("Photon Girl", 95, "Laser Beams")
villain = Villain("Dark Lord", 90, "World Domination")
for character in [hero, villain]:
    character.show_stats()
    character.use_power()
