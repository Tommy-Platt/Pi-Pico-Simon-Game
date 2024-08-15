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
        self.score = 0
        self.colourSequence = []
        self.speed = 0.6

    def clearScreen(self): # Clears screen
        os.system('cls')
    
    # Plays an introductory sequence of colours and sounds when the start button is pressed
    def startupEffects(self):
        while self.gameStarted == False:
            if buttonReset.value() == True:
                ledRed.on()
                self.hw.playSound(noteRed, 0.5)
                sleep(0.1)
                ledRed.off()
                ledBlue.on()
                self.hw.playSound(noteBlue, 0.5)
                sleep(0.1)
                ledBlue.off()
                ledYellow.on()
                self.hw.playSound(noteYellow, 0.5)
                sleep(0.1)
                ledYellow.off()
                ledGreen.on()
                self.hw.playSound(noteGreen, 0.5)
                sleep(0.1)
                ledGreen.off()
                self.gameStarted = True

    # Code for generating the colour sequence    
    def addColours(self):
        randomColour = random.choice(colourList)
        self.colourSequence.append(randomColour)

        self.score = len(self.colourSequence) # Score = length of Simon's sequence
        
        # For every 5 rounds, decrease the speed if speed > 0.1
        if len(self.colourSequence) % 5 == 0:
        
            if self.speed > 0.1:
                self.speed -= 0.1

        # Plays the note and flashes the LED for every colour in Simon's sequence
        for i in self.colourSequence:
            self.hw.playColour(i, self.speed)

        print("Simon Says: " + str(self.colourSequence))
        
    # The function containing the gameplay loop
    def playSimon(self):

        # Resets speed and colourSequence
        self.colourSequence.clear()
        self.speed = 0.6
        
        self.addColours() # Begins the sequence
        
        # Loop for adding colours to the sequence
        while (self.checkColours() == True):
            sleep(1)
            self.addColours()
            
        # Fail sequence to be added
    
    # Checks if the user's button presses equal Simon's sequence
    def checkColours(self):
        
        sequenceCorrect = True # Has the user repeated the sequence
        
        # Loops for every colour in the sequence so far
        for c in self.colourSequence:
            sleep(0.3)
            userColour = self.hw.getButtonPress()
            
            print("You say: " + str(userColour))
            
            # Waits for the user to press a button
            if (userColour == None):
                self.playSimon()
            
            self.hw.playColour(userColour, 0.5) # Lights up the user's colour
            
            # Ends the gameplay loop if the user does not repeat the sequence correctly
            if (userColour != c):
                sequenceCorrect = False
                break
            
        return sequenceCorrect