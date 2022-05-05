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