# The logic and code for the game to work
from machine import *
from time import sleep
from hardware import *
import random, os

class Game:

    # Space for variables

    def __init__(self):
        self.hw = Hardware() # container for hardware functionality

    def clearScreen(self): # Clears screen
        os.system('cls')
    
    # Plays an introductory sequence of colours and sounds
    def startupEffects(self):
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