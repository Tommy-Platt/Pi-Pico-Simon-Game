# Where the game is run from
from pico_simon import *
from hardware import *

# Instantiates the game object from the Game class
game = Game()

game.startupEffects() # Plays the startup sequence

# Start the function for beginning the colour sequence
game.addColours()
game.addColours()
game.addColours()