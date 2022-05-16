import random
import sys
#import class_text -> file must be the same name as the class
from text import Text
from player import Player
from snake import Snake


################ GAME ###########################

Text.print_welcome()
username= input('What is your name? ')
player = Player(username)
Text.confirm_username(player.name)

trip = input('\nWhere do you want to go?\nTrip to Europe (press 1) ')
while trip not in ["1"]:
    Text.wrong_input()
    trip = input('\nWhere do you want to go?\nTrip to Europe (press 1) ')

from snake import european_snakes

generated_snakes = []

if trip == '1':
    Text.print_europe()
    generated_snakes = random.choices(european_snakes, k = 5)
    counter = 0
    for snake in generated_snakes:
        print('\nSnake n°', counter + 1, 'appears.')

        choose_action = input(f'{Text.choose_action()}')
        while choose_action not in ['1', '2', '3', '4', '5', '6']:
            Text.wrong_input()
            choose_action = input(f'{Text.choose_action()}')

        if choose_action == '1':
            generated_snakes[counter].react(player)
            print('Stats for', player.name,':', player.score, 'points', player.health * '♥')

        elif choose_action == '2':                    # Observe
            print(generated_snakes[counter].looks)
            print('While you were looking at the snake, he decided to leave and you lost a chance to boop it.')

        elif choose_action == '3':
            random_index = random.randrange(len(generated_snakes[counter].codex_entry))
            random_codex_entry = generated_snakes[counter].codex_entry[random_index]                                                                            # Codex
            print(generated_snakes[counter].species + '\n' + random_codex_entry)

        elif choose_action == '4':                    # Guess the name
            print('4 - guessing the name')
            print(generated_snakes[counter].species)

        elif choose_action == '5':                    # Leave the snake alone
            print('Žížalka: No pain, no gain. While in a nature is ALWAYS smart to leave a snake alone, in this game you don\'t get anything.')
            print('Stats for', player.name, ':', player.score, 'points', player.health, 'HP')

        elif choose_action == '6':
            print('\nGAME OVER\n', player.name, 'gained', player.score, 'points.') # Exit the game
            player.save_score()
            sys.exit()

        counter += 1

        if player.health <= 0 or counter >= 5:
            print('\nGAME OVER\n' + player.name + ' gained', player.score, 'points.')
            player.save_score()
            #sys.exit()

    more = input('Do you want to try again? ')
    if more.lower in ['yes', 'yy', 'y', 'yeah']:
        print('Žížalka: Ok.')