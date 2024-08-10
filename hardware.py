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

#List of sounds that can be used
soundList = (G2, C2, E3, C4S, E4, A4)

# Assigns notes for each colour in the game
NOTE_YELLOW = C4S
NOTE_BLUE = E4
NOTE_RED = A4
NOTE_GREEN = E3

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

    def __init__(self) -> None:
        pass

    # Plays a set note for a set duration
    def playSound(self, note, duration):
        piezo.freq(note)
        piezo.duty_u16(30000)
        sleep(duration)
        piezo.duty_u16(0)
        sleep(duration)