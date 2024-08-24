from pico_simon import *
from hardware import *
from time import sleep

# Unit tests for the Game class
game = Game()

# Checks if pressing the reset button plays the fanfare
print("Startup effects")
game.startupEffects()

sleep(2)
print("\nstartupEffects complete\n")

# Checks if adding colours to Simon's sequence works & if speed increases every 4 rounds
print("Adding colours")
game.addColours()
game.addColours()
game.addColours()
game.addColours()
game.addColours()
game.addColours()
game.addColours()
game.addColours()

sleep(2)
print("\naddColours complete\n")

# Checks if it can detect if the colour press is correct (will respond incorrect due to addColours being called before and messing with the sequence)
print("Checking colours")
game.score = 22 # Sets a 'fake' score to test if 1's and 10's display on the LED
game.checkColours()

sleep(2)
print("\ncheckColours complete\n")

# Checking if the fail sequence displays the lights, score and "correct" sequence
print("Fail sequence")
game.failSequence()

sleep(2)
print("\nfailSequence complete\n")

# Unit tests for the Hardware class
hardware = Hardware()

# Sees if each note in soundList can be played with the piezo
print("Playing sound")
for n in soundList:
    hardware.playSound(n, 0.5)
    hardware.playSound(n, 0.2)

sleep(2)
print("\nplaySound complete\n")

# Sees if each LED can turn on and off
print("Lighting LEDs")
for c in hardware.components:
    hardware.lightLed(c, True)
    sleep(0.5)
    hardware.lightLed(c, False)

sleep(2)
print("\nlightLED complete\n")

# Sees if each each LED + corresponding note can be played
print("Playing colours (LED + sound)")
for c in hardware.components:
    hardware.playColour(c, 0.5)
    hardware.playColour(c, 0.2)

sleep(2)
print("\nplayColour complete\n")

# Gets user input and prints it for each button press
print("Getting user button presses")
hardware.getButtonPress()
sleep(1)
hardware.getButtonPress()
sleep(1)
hardware.getButtonPress()
sleep(1)
hardware.getButtonPress()

sleep(2)
print("\ngetButtonPress complete\n")

# Testing for unexpected, extreme, negative and boundary values
hardware.playSound(100000000000, 0.5)
hardware.playSound(-1, 0.5)
hardware.playSound("G4", 0.5)
hardware.playSound(G4, 0)
hardware.playSound(G4, -1)
hardware.playSound(G4, 100000000000)

hardware.lightLed(100000000000, True)
hardware.lightLed(100000000000, False)
hardware.lightLed(-1, True)
hardware.lightLed(-1, False)
hardware.lightLed(YELLOW, True)
hardware.lightLed(YELLOW, False)
hardware.lightLed("yellow", True)
hardware.lightLed("yellow", False)

hardware.playColour(YELLOW, 0.5)
hardware.playColour(YELLOW, 0.2)
hardware.playColour("dog", 0.5)
hardware.playColour("dog", 0.2)
hardware.playColour(100000000000, 0.5)
hardware.playColour(100000000000, 0.2)
hardware.playColour(-1, 0.5)
hardware.playColour(-1, 0.2)