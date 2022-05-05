class Snake:
    def __init__(self):
        self.venomous = False
        self.continent = None
        self.codex_entry = []
        self.looks = ''
        self.species = ''
        self.reactions = ['bite', 'hiss', 'coil']           # flip tongue, yawn, staying still
        self.reaction_matrix = [0, 0, 100]

    def react(self, player):
        random_reaction = random.choices(self.reactions, self.reaction_matrix)[0]
        getattr(self, random_reaction)(player)

    def bite(self, player):
        if self.venomous:
            damage = random.randint(1, 3)
            score = -5
            print('Snake bit you! You lost', score, ' points and', damage, 'HP.')
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