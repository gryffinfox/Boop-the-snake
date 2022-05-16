import random
from player import Player

european_snakes = []

class Snake:
    def __init__(self, venomous, continent, looks, species, reaction_matrix):
        self.venomous = venomous
        self.continent = continent
        self.codex_entry = []
        self.looks = looks
        self.species = species
        self.reactions = ['bite', 'hiss', 'coil']           # add flip tongue, yawn, staying still?
        self.reaction_matrix = reaction_matrix

    def react(self, player):
        random_reaction = random.choices(self.reactions, self.reaction_matrix)[0]
        getattr(self, random_reaction)(player)

    def bite(self, player):
        if self.venomous:
            damage = random.randint(1, 3)
            score = -5
        else:
            damage = random.randint(0, 1)
            score = -2

        player.suffer(damage)
        player.add_score(score)
        print('Snake bit you! You lost', score, 'points and', damage, 'HP.')

    def hiss(self, player):
        player.suffer(1)
        score = 5
        player.add_score(score)
        print('Snake hissed at you! You gained', score, 'points and lost 1 HP.')

    def coil(self, player):
        score = 10
        player.add_score(score)
        print('Snake coiled! You gained', score, ' points.')


###### BOA South America, reaction matrix [50, 40, 10] ########
#### Erycinae Europe, reaction matric [5, 5, 90] ####
sand_boa = Snake(False, 'Europe', 'Usually burried.', 'The Sand boa - Eryx jaculus', [5, 5, 90])
sand_boa.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
european_snakes.append(sand_boa)

#### Colubrid Europe, reaction matrix [30, 40, 30] ####
cat_snake = Snake(True, 'Europe', 'I am a danger noodle, fear me! SssssSSSSsss',
                  'The Cat snake - Telescopus fallax', [30, 40, 30])
cat_snake.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
european_snakes.append(cat_snake)

grass_snake = Snake(False, 'Europe', 'I may looks scary but I am a sweetheart. '
                    'Now give me some fishsssss!', 'The Grass snake - Natrix natrix', [30, 40, 30])
grass_snake.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
european_snakes.append(grass_snake)

smooth_snake = Snake(False, 'Europe', 'I an UBS - universal brown snake. Sometimes hisssssss.',
                     'The Smooth snake - Coronella austriaca', [30, 40, 30])
smooth_snake.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
european_snakes.append(smooth_snake)

horseshoe_whip = Snake(False, 'Europe', 'SsssSsspaghetti snek but ok.',
                        'The Horseshoe whip snake - Hemorrhois hippocrepis', [30, 40, 30])
horseshoe_whip.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
european_snakes.append(horseshoe_whip)

#### Viper, Europe, reaction matrix [60, 30, 10] #####
common_adder = Snake(True,'Europe', 'I am a scary snek! SSSSSssssss!', 'The Common adder - Vipera berus', [60, 30, 10])
common_adder.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
european_snakes.append(common_adder)

asp_viper = Snake(True,'Europe', 'I am a tiny scary snek! Sssss ss s sss', 'The Asp viper - Vipera aspis', [60, 30, 10])
asp_viper.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
european_snakes.append(asp_viper)

vipera_renardi = Snake(True,'Europe', 'I can look differently according to the subspecies. Still scary snake! SSSSSSss ss sss!',
                       '\nVipera renardi', [60, 30, 10])
vipera_renardi.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
european_snakes.append(vipera_renardi)