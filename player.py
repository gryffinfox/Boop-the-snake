class Player:
    def __init__(self, name):
        self.name = name
        self.health = 5
        self.experience = 0
        self.score = 0

    def suffer(self, health = 1):
        self.health = self.health - health

    def set_name(self, username):
        self.name = username

    def add_score(self, points):
        self.score = self.score + points

    def gain_experience(self, exp):
        self.experience += exp

    def save_score(self):
        with open('highscore.txt', 'a') as file:
            file.write(f'\n{self.name} : {self.score}')