class Text:
    def __init__(self):
        self.name_confirmation =
        self.choose_action = ('\nWhat do you want to do?\n'
                                      'Boop the snake (press 1)\n'
                                      'Observe the snake (press 2)\n'
                                      'Search in the codex (press 3)\n'
                                      'Guess (press 4)\n'
                                      'Leave the snake alone (press 5)\n'
                                      'Exit the game (press 6)\n ')
    def welcome (self):
        print('Welcome to the snake booping game!'
              'I am Žížalka and I will be your guide.')

    def name_confirmation(self):
        print('Žížalka:', who_is_playing, ','
            'how pretty! Let\'s go for a trip.')

    def choose_action(self):
        print('\nWhat do you want to do?\n'
                'Boop the snake (press 1)\n'
                'Observe the snake (press 2)\n'
                'Search in the codex (press 3)\n'
                'Guess (press 4)\n'
                'Leave the snake alone (press 5)\n'
                'Exit the game (press 6)\n')

    def wrong_input(self):
        print('\nŽížalka: Did the cat walk on your keyboard? To go for a trip, '
              'type the number of the trip and press enter.')

    def europe(self):
        print('Žížalka: Welcome in Europe! '
            'You will encouter five snakes a with each you need to decide if you boop them or not.'
            '\nBooping will get you points but it can also cost you lives. Not booping will gain you nothing.'
            '\nGame is over if you run out of lives or if you finish encountering all snakes.')

    def wrong_input_two(self):
        print('\nŽížalka: I don\'t accept different answers than 1 (for boop), 2 (for observing), '
              '3 (for codex), 4 (for guessing) or 5 (to leave the game).')