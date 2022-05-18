# Rename the class
# Add all the strings
# Rename the methods

class Text:
    @staticmethod
    def print_welcome():
        print('Welcome to the snake booping game!'
              'I am Žížalka and I will be your guide.')

    @staticmethod
    def confirm_username(username):
        print('Žížalka:', username, 'how pretty! Let\'s go for a trip.')

    @staticmethod
    def choose_action():                        #Rename
        return '\nWhat do you want to do?\n'\
                + 'Boop the snake (press 1)\n'\
                + 'Observe the snake (press 2)\n'\
                + 'Search in the codex (press 3)\n'\
                + 'Guess (press 4)\n'\
                + 'Leave the snake alone (press 5)\n'\
                + 'Exit the game (press 6)\n'

    @staticmethod
    def wrong_input():
        print('\nŽížalka: Did the cat walk on your keyboard? To go for a trip, '
              'type the number of the trip and press enter.')

    @staticmethod
    def print_europe():
        print('Žížalka: Welcome in Europe! '
            'You will encouter five snakes a with each you need to decide if you boop them or not.'
            '\nBooping will get you points but it can also cost you lives. Not booping will gain you nothing.'
            '\nGame is over if you run out of lives or if you finish encountering all snakes.')

    @staticmethod
    def wrong_input_two():
        print('\nŽížalka: I don\'t accept different answers than 1 (for boop), 2 (for observing), '
              '3 (for codex), 4 (for guessing) or 5 (to leave the game).')