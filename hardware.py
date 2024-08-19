# Setting up variables e.g. for pins
from machine import *
from time import sleep
import random, os

# Note frequencies to be used
G2 = 98 
C2 = 65 
E3 = 165 
C4S = 277 
E4 = 330 
A4 = 440 
G4 = 392

#List of sounds that can be used
soundList = (G2, C2, E3, C4S, E4, A4)

# Assigns notes for each colour in the game
noteYellow = C4S
noteBlue = E4
noteRed = A4
noteGreen = E3

# GPIO pin numbers for LEDs, buttons and passive buzzer.
ledRed = Pin(10, Pin.OUT)
ledBlue = Pin(11, Pin.OUT)
ledYellow = Pin(12, Pin.OUT)
ledGreen = Pin(13, Pin.OUT)

buttonGreen = Pin(17, Pin.IN)
buttonYellow = Pin(19, Pin.IN)
buttonBlue = Pin(22, Pin.IN)
buttonRed = Pin(27, Pin.IN)

buttonReset = Pin(16, Pin.IN)
piezo = PWM(3)

# Text for colour constants
BLUE = 'blue'
GREEN = 'green'
RED = 'red'
YELLOW = 'yellow'

# Array of all colours.
colourList = [GREEN, YELLOW, BLUE, RED]

# Class that contains all of the functionality of the hardware e.g. playing noise
class Hardware:

    def __init__(self):
        # Creates a dictionary for each colour's button, LED and note
        self.components = {}
        self.components['blue'] = (buttonBlue, ledBlue, noteBlue)
        self.components['yellow'] = (buttonYellow, ledYellow, noteYellow)
        self.components['red'] = (buttonRed, ledRed, noteRed)
        self.components['green'] = (buttonGreen, ledGreen, noteGreen)

    # Plays a set note for a set duration
    def playSound(self, note, duration):
        piezo.freq(note)
        piezo.duty_u16(30000)
        sleep(duration)
        piezo.duty_u16(0)
        sleep(duration)

    # Lights an LED from the components dictionary
    def lightLed(self, colour, state):

        led = self.components[colour]
        led[1].value(state)

    # Plays a colour and its corresponding note for a set duration
    def playColour(self, colour, duration):
        
        self.lightLed(colour, True)
        note = self.components[colour]
        self.playSound(note[2], duration)
        self.lightLed(colour, False)
        sleep(0.2)
        
    # Gets a button press from the user
    def getButtonPress(self):
        
        # Loops through the available colours and checks if each one has been pressed. Returns the pressed colour
        while True:
            for c in colourList:
                buttonValue = self.components[c][0].value()
                
                if (buttonValue == 1):
                    return c
            
            buttonValue = buttonReset.value()
            
            sleep(0.1)
