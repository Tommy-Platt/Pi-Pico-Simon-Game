# The logic and code for the game to work
from machine import *
from time import sleep
from hardware import *
import random, os

class Game:

    # Space for variables

    def __init__(self):
        self.hw = Hardware() # container for hardware functionality
        self.gameStarted = False

    def clearScreen(self): # Clears screen
        os.system('cls')
    
    # Plays an introductory sequence of colours and sounds when the start button is pressed
    def startupEffects(self):
        while self.gameStarted == False:
            if buttonReset.value() == True:
                ledRed.on()
                self.hw.playSound(NOTE_RED, 0.5)
                sleep(0.1)
                ledRed.off()
                ledBlue.on()
                self.hw.playSound(NOTE_BLUE, 0.5)
                sleep(0.1)
                ledBlue.off()
                ledYellow.on()
                self.hw.playSound(NOTE_YELLOW, 0.5)
                sleep(0.1)
                ledYellow.off()
                ledGreen.on()
                self.hw.playSound(NOTE_GREEN, 0.5)
                sleep(0.1)
                ledGreen.off()
                self.gameStarted = True

    # Code for generating the colour sequence
    #----------------------------------------
    # Define the score variable in the __init__ function
    # Randomly select a colour (randomColour) from colourList (in hardware)
    # Add the selected colour to a new list (colourSequence)
    # Print colourSequence in the terminal + what the list means so we can test how it works
