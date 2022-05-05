import random
import sys
import class_player
import class_snake
import class_text
import class_boa
import class_colubrid
import class_viper

all_snakes = []

################ GAME ###########################

welcome()
who_is_playing = input('What is your name? ')
username = Player(who_is_playing)
name_confirmation()

trip = input('\nWhat do you choose?\nTrip to Europe (press 1) ')
while trip != range(0-1):
    continue

generated_snakes = []

if trip == '1':
    europe()
    generated_snakes = random.choices(all_snakes, k = 5)
    counter = 0
    for snake in generated_snakes:
        print('\nSnake n°', counter + 1, 'appears.')

    while choose_action != range(0-5):
        choose_action = input(choose_action())
        continue

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

    counter += 1

    if username.health <= 0 or counter >= 5:
        print('\nGAME OVER\n' + username.name + ' gained', username.score, 'points.')
        username.save_score()
        #sys.exit()

    more = input('Do you want to try again? ')
    if more.lower in ['yes', 'yy', 'y', 'yeah']:
        print('Žížalka: Ok.')

    else:
        break