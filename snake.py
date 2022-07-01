import random

loaded_snakes = []
generated_snakes = []

class Snake:
    def __init__(self, english, latin, venomous, continent, looks, codex_entry, reaction_matrix):
        self.name = english + ' - ' + latin
        self.venomous = venomous
        self.continent = continent
        self.codex_entry = codex_entry
        self.looks = looks
        # add flip tongue, yawn, staying still?
        self.reactions = ('bite', 'hiss', 'coil')
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


#BOA South America, reaction matrix [50, 40, 10] ########
#Erycinae Europe, reaction matric [5, 5, 90] ####
#Colubrid Europe, reaction matrix [30, 40, 30] ####
#Viper, Europe, reaction matrix [60, 30, 10] #####
