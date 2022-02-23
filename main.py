import random
import sys

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
        self.experience += exp

    def save_score(self):
        with open('highscore.txt', 'a') as file:
            file.write(f'\n{self.name} : {self.score}')

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
        print('Snake hissed at you! You gained 5 points and lost 1 HP.')

    def coil(self, player):
        player.add_score(10)
        print('Snake coiled! You gained 10 points.')

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
cat_snake.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
all_snakes.append(cat_snake)

grass_snake = Colubrid('I may looks scary but I am a sweetheart. Now give me some fishsssss!', 'The Grass snake - Natrix natrix' )
grass_snake.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
all_snakes.append(grass_snake)

smooth_snake = Colubrid('I an UBS - universal brown snake. Sometimes hisssssss.', 'The Smooth snake - Coronella austriaca')
smooth_snake.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
all_snakes.append(smooth_snake)

horseshoe_whip = Colubrid('SsssSsspaghetti snek but ok.', 'The Horseshoe whip snake - Hemorrhois hippocrepis')
horseshoe_whip.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
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
sand_boa.codex_entry = ['fact 1', 'fact 2', 'fact 3', 'fact 4']
all_snakes.append(sand_boa)

################ GAME ###########################
print('Welcome to the snake booping game! I am Žížalka and I will be your guide.')
who_is_playing = input('What is your name? ')
username = Player(who_is_playing)

print('Žížalka:', who_is_playing,', how pretty! Let\'s go for a trip.')
while True:
    level = input('\nWhat do you choose?\nTrip to Europe (press 1) ')
    generated_snakes = []

    if level == '1':
        print('Žížalka: Welcome in Europe! You will encouter five snakes a with each you need to decide if you boop them or not.'
            '\nBooping will get you points but it can also cost you lives. Not booping will gain you nothing.'
            '\nGame is over if you run out of lives or if you finish encountering all snakes.')
        generated_snakes = random.choices(all_snakes, k = 5)

        counter = 0
        for snake in generated_snakes:
            print('\nSnake n°', counter + 1, 'appears.')

            while True:

                choose_action = input('\nWhat do you want to do?\n'
                                      'Boop the snake (press 1)\n'
                                      'Observe the snake (press 2)'
                                      'Search in the codex (press 3)\n'
                                      'Guess (press 4)\n'
                                      'Leave the snake alone (press 5)\n'
                                      'Exit the game (press 6)\n ')

                if choose_action == '1':
                    generated_snakes[counter].react(username)
                    print('Stats for', username.name,':', username.score, 'points', username.health * '♥')
                    break

                elif choose_action == '2':                    # Observe
                    print(generated_snakes[counter].looks)
                    print('While you were looking at the snake, he decided to leave and you lost a chance to boop it.')
                    break

                elif choose_action == '3':
                    random_index = random.randrange(len(generated_snakes[counter].codex_entry))
                    random_codex_entry = generated_snakes[counter].codex_entry[random_index]                                                                            # Codex
                    print(generated_snakes[counter].species + '\n' + random_codex_entry)
                    break

                elif choose_action == '4':                    # Guess the name
                    print('4 - guessing the name')
                    break

                elif choose_action == '5':                    # Leave the snake alone
                    print('Žížalka: No pain, no gain. While in a nature is ALWAYS smart to leave a snake alone, in this game you don\'t get anything.')
                    print('Stats for', username.name, ':', username.score, 'points', username.health, 'HP')
                    break

                elif choose_action == '6':
                    print('\nGAME OVER\n', username.name, 'gained', username.score, 'points.') # Exit the game
                    username.save_score()
                    sys.exit()

                else:
                    print('\nŽížalka: I don\'t accept different answers than 1 (for boop), 2 (for observing), '
                          '3 (for codex), 4 (for guessing) or 5 (to leave the game).')

            counter += 1
        if username.health <= 0 or counter >= 5:
            print('\nGAME OVER\n' + username.name + ' gained', username.score, 'points.')
            username.save_score()
            #sys.exit()

    else:
        print('\nŽížalka: Did the cat walk on your keyboard? To go for a trip, type the number of the trip and press enter.')

    more = input('Do you want to play again? ')
    if more.lower in ['yes', 'yy', 'y', 'yeah']:
        print('Žížalka: Ok.')
    else:
        break