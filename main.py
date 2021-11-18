import random
all_snakes = []

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
        #self.experience += exp
        self.experience = self.experience + exp

    def save_score(self, username, points):
        with open('highscore.txt', 'a') as file:
            content = file.write(username, points)

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
        getattr(self, random_reaction)

    def bite(self, player):
        if self.venomous:
            damage = random.randint(1, 3)
            player.add_score(-5)
            print('Snake bit you! You lost 5 points and', damage, 'HP.')
        else:
            damage = random.randint(0, 1)
            player.add_score(-2)
            print('Snake bit you! You lost 2 points and', damage, 'HP.')

        player.suffer(damage)

    def hiss(self, player):
        player.suffer(1)
        player.add_score(5)

    def coil(self, player):
        player.add_score(10)

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
all_snakes.append(common_adder)

asp_viper = Viper('I am a tiny scary snek! Sssss ss s sss', 'The Asp viper - Vipera aspis')
all_snakes.append(asp_viper)

vipera_renardi = Viper('I can look differently according to the subspecies. Still scary snake! SSSSSSss ss sss!', 'Vipera renardi')
all_snakes.append(vipera_renardi)

class Colubrid(Snake):
    def __init__(self, looks, species, codex_entry = []):
        super().__init__()
        self.venomous = False
        self.continent = 'Europe'
        self.codex_entry = []
        self.looks = looks
        self.species = species
        self.reaction_matrix = [30, 40, 30]

cat_snake = Colubrid('I am a danger noodle, fear me! SssssSSSSsss', 'The Cat snake - Telescopus fallax')
cat_snake.venomous = True
all_snakes.append(cat_snake)

grass_snake = Colubrid('I may looks scary but I am a sweetheart. Now give me some fishsssss!', 'The Grass snake - Natrix natrix' )
all_snakes.append(grass_snake)

smooth_snake = Colubrid('I an UBS - universal brown snake. Sometimes hisssssss.', 'The Smooth snake - Coronella austriaca')
all_snakes.append(smooth_snake)

horseshoe_whip = Colubrid('SsssSsspaghetti snek but ok.', 'The Horseshoe whip snake - Hemorrhois hippocrepis')
all_snakes.append(horseshoe_whip)

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
all_snakes.append(sand_boa)

################ GAME ###########################
print('Welcome to the snake booping game! I am Žížalka and I will be your guide.')
who_is_playing = input('What is your name? ')
username = Player(who_is_playing)

print('Žížalka:', who_is_playing,', how pretty! Let\'s go for a trip.')
level = int(input('\nWhat do you choose?\nTrip to Europe (press 1) '))
print('Žížalka: Welcome in Europe! You will encouter five snakes a with each you need to decide if you boop them or not.'
      '\nBooping will get you points but it can also cost you lives. Not booping will gain you nothing.'
      '\nGame is over if you run out of lives or if you finish encountering all snakes.')
generated_snakes = []

if level == 1:
    generated_snakes = random.choices(all_snakes, k = 5)

counter = 0
stopper = True
for snake in generated_snakes:
    print('\nSnake n°', counter + 1, 'appears.')
    while stopper:
        boop = input('Do you want to boop it? Y/N ')
        if boop.lower() in ['yes', 'y', 'ye', 'yy']:

            generated_snakes[counter].react(username)
            stopper = False
            if username.health <= 0:
                print('GAME OVER\n', username, 'gained', username.score, 'points.')
        elif boop.lower() in ['no', 'n', 'nn']:
            stopper = False
            print('Žížalka: No pain, no gain. While in a nature is ALWAYS smart to leave snake alone, in this game you dont get anything.')
        else:
            print('Žížalka: I dont accept different answers then yes or no.')
        counter += 1


