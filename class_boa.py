class Boa(Snake):
    def __init__(self, looks, species, codex_entry = []):
        super().__init__()
        self.venomous = False
        self.continent = 'South America'
        self.codex_entry = codex_entry
        self.looks = looks
        self.species = species
        self.reaction_matrix = [50, 40, 10]

class Erycinae(Boa):
    class Boa(Snake):
        def __init__(self, looks, species, codex_entry = []):
            super().__init__(self)
            self.continent = 'Europe'
            self.codex_entry = codex_entry
            self.looks = looks
            self.species = species
            self.reaction_matrix = [5, 5, 90]

sand_boa = Erycinae('Usually burried.', 'The Sand boa - Eryx jaculus')
sand_boa.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
all_snakes.append(sand_boa)