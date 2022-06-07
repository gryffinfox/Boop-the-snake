# Add all the strings
# Rename the methods

class Narrator:
    @staticmethod
    def print_welcome():
        print('Welcome to the snake booping game!'
              'I am Žížalka and I will be your guide.')

    @staticmethod
    def confirm_username(username):
        print('Žížalka:', username, 'how pretty! Let\'s go for a trip.')

    @staticmethod
    def choose_action():
        return'\nWhat do you want to do?\n'\
              'Boop the snake (press 1)\n'\
              'Observe the snake (press 2)\n'\
              'Search in the codex (press 3)\n'\
              'Guess (press 4)\n'\
              'Leave the snake alone (press 5)\n'\
              'Exit the game (press 6)\n'

    @staticmethod
    def wrong_input():
        print('\nŽížalka: Did the cat walk on your keyboard? To go for a trip, '
              'type the number of the trip and press enter.')

    @staticmethod
    def print_europe():
        print('Žížalka: Welcome in Europe! '
            'You will encouter five european snakes a with each you need to decide what you are going to do.'
            '\nBooping will get you points but it can also cost you lives. Leaving the snake alone (while smart in the nature) doesn\'t give you points but it keeps you healthy.'
            '\nGame is over if you run out of lives or if you finish encountering all snakes.')

    @staticmethod
    def wrong_input_two():
        print('\nŽížalka: I don\'t accept different answers than 1 (for boop), 2 (for observing), '
              '3 (for codex), 4 (for guessing) or 5 (to leave the game).')

    @staticmethod
    def print_stats(Player):
        print('Stats for', Player.name, ':', Player.score, 'points', Player.health * '♥')

    #@staticmethod
    #def display_looks(counter):
        #print(generated_snakes[counter].looks)

    @staticmethod
    def print_snake_leaving():
        return 'While you were looking at the snake, he decided to leave and you lost a chance to boop it.'

    @staticmethod
    def leave_snake_alone():
        return 'Žížalka: No pain, no gain. While in a nature is ALWAYS smart to leave a snake alone, in this game you don\'t get anything.'