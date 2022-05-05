class Viper(Snake):
    def __init__(self, looks, species, codex_entry = []):
        super().__init__()
        self.venomous = True
        self.continent = 'Europe'
        self.codex_entry = codex_entry
        self.looks = looks
        self.species = species
        self.reaction_matrix = [60, 30, 10]

common_adder = Viper('I am a scary snek! SSSSSssssss!', 'The Common adder - Vipera berus')
common_adder.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
all_snakes.append(common_adder)

asp_viper = Viper('I am a tiny scary snek! Sssss ss s sss', 'The Asp viper - Vipera aspis')
asp_viper.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
all_snakes.append(asp_viper)

vipera_renardi = Viper('I can look differently according to the subspecies. Still scary snake! SSSSSSss ss sss!',
                       '\nVipera renardi')
vipera_renardi.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
all_snakes.append(vipera_renardi)