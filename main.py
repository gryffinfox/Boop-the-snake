import random
import sys
#import class_text -> file must be the same name as the class
from text import Text
from player import Player
from snake import Snake
from snake import european_snakes

def generate_snakes(trip):
    if trip == '1':
        Text.print_europe()
        return random.choices(european_snakes, k = 5)
    else:
        raise ValueError(trip)

################ GAME ###########################

Text.print_welcome()
username= input('What is your name? ')
player = Player(username)
Text.confirm_username(player.name)

playerWantsToPlay = True

while playerWantsToPlay:

    trip = 0
    while True:
        trip = input('\nWhere do you want to go?\nTrip to Europe (press 1) ')
        if trip in ["1"]:
            break
        else:
            Text.wrong_input()

    generated_snakes = generate_snakes(trip)

    counter = 0
    for snake in generated_snakes:
        print('\nSnake n°', counter + 1, 'appears.')

        while True:
            choose_action = input(f'{Text.choose_action()}')
            if choose_action in ['1', '2', '3', '4', '5', '6']:
                break
            else:
                Text.wrong_input()

        # boop
        if choose_action == '1':
            generated_snakes[counter].react(player)
            print('Stats for', player.name,':', player.score, 'points', player.health * '♥')

        # observe
        elif choose_action == '2':
            print(generated_snakes[counter].looks)
            print('While you were looking at the snake, he decided to leave and you lost a chance to boop it.')

        # search in the codex
        elif choose_action == '3':
            random_index = random.randrange(len(generated_snakes[counter].codex_entry))
            random_codex_entry = generated_snakes[counter].codex_entry[random_index]
            print(generated_snakes[counter].name + '\n' + random_codex_entry)

        # guess
        elif choose_action == '4':
            print('4 - guessing the name')
            print(generated_snakes[counter].name)

        # leave it
        elif choose_action == '5':
            print('Žížalka: No pain, no gain. While in a nature is ALWAYS smart to leave a snake alone, in this game you don\'t get anything.')
            print('Stats for', player.name, ':', player.score, 'points', player.health, 'HP')

        # exit
        elif choose_action == '6':
            print('\nGAME OVER\n', player.name, 'gained', player.score, 'points.')
            player.save_score()
            sys.exit()

        counter += 1

        if player.health <= 0 or counter >= 5:
            print('\nGAME OVER\n' + player.name + ' gained', player.score, 'points.')
            player.save_score()
            break

    more = input('Do you want to try again? ')
    if more.lower in ['yes', 'yy', 'y', 'yeah']:
        print('Žížalka: Ok.')
    else:
        playerWantsPlay = False



