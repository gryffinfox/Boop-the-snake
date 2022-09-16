# The hangman game

# converting the secret word into a set, then we use the join() to create a string of unique letters
def get_unique_letters(word):
    return ''.join(set(word))

##########################################
def get_hangsnake_stage(remaining_attempts):
    max_attempts = 6
    stages = ['>-8/\/\/\/\/\/\/', '>-8/1\/\/\/\/\/\/', '>-8/1\/2\/\/\/\/\/', '>-8/1\/2\/3\/\/\/\/',
              '>-8/1\/2\/3\/4\/\/\/', '>-8/1\/2\/3\/4\/5\/\/', '>-8/1\/2\/3\/4\/5\/6\/']

    return stages[max_attempts - remaining_attempts]
#####################################

def print_secret_word(secret_word, guessed_letters, default_letters):
    for letter in secret_word:
        if letter in guessed_letters or letter in default_letters:
          print(' {} '.format(letter), end='')
        else:
            # end parameter in the print() is there to have each character on the same line
            print(' _ ', end='')
    print('\n')

#######################################

def is_guess_in_secret_word(guess, secret_word):
    #
    if len(guess) > 1: #or not guess.isalpha():
        print('Žížalka: Concentrate! Only single letters are allowed. Try again.')
        guess = input('Guess a letter: ')
    else:
        if guess in secret_word:
            return True
        else:
            return False

########################################

def play_game(snake_name):
    print('Žížalka: Ready to play a game? This one works exactly like the hangman game. '
          'Let\'s see if you can guess this word!\n')
    remaining_attempts = 6
    default_letters = ' ' + '-'
    guessed_letters = ''
    secret_word = snake_name.lower()
    print(secret_word)
    print_secret_word(secret_word, guessed_letters, default_letters)

    while remaining_attempts > 0 and len(guessed_letters) < len(get_unique_letters(secret_word)):
        guess = input('Guess a letter: ')
        guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)

        if guess_in_secret_word:
            if guess in guessed_letters:
                print('You have already guessed the letter {}'.format(guess))
            else:
                print('Yes! The letter {} is part of the secret word'.format(guess))
                guessed_letters += guess
        else:
            print('No! The letter {} is not part of the secret word'.format(guess))
            remaining_attempts -= 1

        print(get_hangsnake_stage(remaining_attempts))
        print_secret_word(secret_word, guessed_letters, default_letters)
        print('\n\nLetters guessed:', guessed_letters)
        #print('\n\nNumber of letters guessed: {}\n'.format(len(guessed_letters)))

    if len(guessed_letters) == len(get_unique_letters(secret_word)):
        print("+++ Well done, you have won this game! +++\n")
    else:
        print("--- Sorry, you have lost this game! ---\n")
