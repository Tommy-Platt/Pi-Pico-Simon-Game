# Where the game is run from
from pico_simon import *
from hardware import *

# Instantiates the game object from the Game class
game = Game()

game.startupEffects() # Plays the startup sequence

# Plays Simon's sequence of colours 3 times e.g. 1, 1 2, 1 2 3
game.addColours()
game.addColours()
game.addColours()