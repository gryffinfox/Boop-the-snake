#info on the beggining what should player have installed?

import random
import sys
#import class_text -> file must be the same name as the class
from narrator import Narrator
from player import Player
from snake import Snake
from snake import european_snakes

def generate_snakes(trip):
    if trip == '1':
        Narrator.print_europe()
        return random.choices(european_snakes, k=5)
    else:
        raise ValueError(trip)

################ GAME ###########################

Narrator.print_welcome()
username= input('What is your name? ')
player = Player(username)
Narrator.confirm_username(player.name)

playerWantsToPlay = True

while playerWantsToPlay:
    trip = 0
    while True:
        trip = input('\nWhere do you want to go?\nTrip to Europe (press 1) ')
        if trip  in ["1"]:
            break

        else:
            Narrator.wrong_input()

    generated_snakes = generate_snakes(trip)

    counter = 0
    for snake in generated_snakes:
        print('\nSnake n°', counter + 1, 'appears.')

        #Player chooses what to do
        while True:
            choose_action = input(f'{Narrator.choose_action()}')

            if choose_action in ['1', '2', '3', '4', '5', '6']:
                break
            else:
                Narrator.wrong_input()

        #Boop
        if choose_action == '1':
            generated_snakes[counter].react(player)
            Narrator.print_stats(player)
            #print('Stats for', player.name,':', player.score, 'points', player.health * '♥')

        #Observe
        elif choose_action == '2':
            print(generated_snakes[counter].looks)
            #Text.display_looks(counter)
            Narrator.print_snake_leaving()

        #Search in codex
        elif choose_action == '3':
            random_index = random.randrange(len(generated_snakes[counter].codex_entry))
            random_codex_entry = generated_snakes[counter].codex_entry[random_index]
            print(generated_snakes[counter].species + '\n' + random_codex_entry)

        #Guess the name
        elif choose_action == '4':
            print('4 - guessing the name')
            guess = input('Who am I?\n')
            if generated_snakes[counter].species in guess:
                print('Žížalka: Bravo!')
                player.add_score(10)
                Narrator.print_stats(player)
            else:
                print('Žížalka: Nope! Next time you get it right!')

        #Leave the snake alone
        elif choose_action == '5':
            Narrator.leave_snake_alone()
            print('Stats for', player.name, ':', player.score, 'points', player.health, 'HP')

        #Game over
        elif choose_action == '6':
            print('\nGAME OVER\n', player.name, 'gained', player.score, 'points.')
            player.save_score()
            sys.exit()

        counter += 1

        if player.health <= 0 or counter >= 5:
            print('\nGAME OVER\n' + player.name + ' gained', player.score, 'points.')
            player.save_score()
            break

    #Play again?
    play_again = input('Do you want to try again? ')
    if play_again.lower in ['yes', 'yy', 'y', 'yeah']:
        print('Žížalka: Ok.')
    else:
        playerWantsToPlay = False