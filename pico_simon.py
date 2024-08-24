# The logic and code for the game to work
from machine import *
from time import sleep
from hardware import *
import random, os

# Class containing function related to gameplay functionality e.g. checking user input
class Game:

    def __init__(self):
        self.hw = Hardware() # Container for hardware functionality
        self.gameStarted = False # Boolean checker for if the game is running
        self.score = 0 # User score
        self.colourSequence = [] # List variable for Simon's colour sequence
        self.speed = 0.6 # Speed of the game
    
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
                sleep(1)
                self.gameStarted = True

    # Code for generating the colour sequence    
    def addColours(self):
        randomColour = random.choice(colourList)
        self.colourSequence.append(randomColour)
        
        # For every 5 rounds, decrease the speed if speed > 0.1
        if len(self.colourSequence) % 4 == 0:
        
            if self.speed > 0.1:
                self.speed -= 0.1

        # Plays the note and flashes the LED for every colour in Simon's sequence
        for i in self.colourSequence:
            self.hw.playColour(i, self.speed)

        print("Simon Says: " + str(self.colourSequence))
        
    # The function containing the gameplay loop
    def playSimon(self):
        # Plays the startup effects before the game continues
        self.startupEffects()

        # Resets variables for the game upon starting
        self.colourSequence.clear()
        self.speed = 0.6
        self.score = 0
        
        self.addColours() # Begins the sequence
        
        # Loop for adding colours to the sequence
        while (self.checkColours() == True):
            self.score = len(self.colourSequence) # Score = length of Simon's sequence if user's matches
            sleep(0.3)
            print("\033c") # Clears screen
            self.addColours()

        # Fail sequence plays if user fails the sequence, allows game to restart
        else:    
            self.failSequence()
            self.gameStarted = False
            self.playSimon()
                    
    # Checks if the user's button presses equal Simon's sequence
    def checkColours(self):

        sequenceCorrect = True # Has the user repeated the sequence?
        
        # Loops for every colour in the sequence so far
        for c in self.colourSequence:
            sleep(0.1)
            userColour = self.hw.getButtonPress() # Gets user's input for each colour in the sequence
            
            # Waits for the user to press a button
            if (userColour == None):
                self.playSimon()
            
            self.hw.playColour(userColour, 0.5) # Lights up the user's colour
            
            # Ends the gameplay loop if the user does not repeat the sequence correctly
            if (userColour != c):
                sequenceCorrect = False
                break
            
        return sequenceCorrect
    
    # Plays a lightshow for when the user fails
    def failSequence(self):
        
        sleep(0.5)

        for c in colourList:
            self.hw.lightLed(c, True)

        self.hw.playSound(G2, 0.25) # Fail notes
        self.hw.playSound(C2, 0.5) # -----------

        sleep(0.5)

        for c in colourList:
            self.hw.lightLed(c, False)

        print("Incorrect! Simon said: " + str(self.colourSequence)) # Print's correct sequence
        
        # Lights up the LEDs for correct sequence
        for i in self.colourSequence:
            self.hw.playColour(i, self.speed)

        sleep(1)

        self.hw.playSound(C2, 0.5) # Sounds notify user that the score will now display
        self.hw.playSound(E3, 0.5) # --------------------------------------------------
        self.hw.playSound(G4, 0.5) # --------------------------------------------------

        self.scoreOnes = self.score % 10 # Gets the one's place of the score
        self.scoreTens = (self.score // 10) % 10 # Gets the tens's place of the score
        
        sleep(1)

        print("Your score was: " + str(self.score)) # Displays score in terminal

        # Displays the score as green & yellow flashes corresponding to the digits of the number
        for o in range(self.scoreOnes):
            self.hw.playColour(GREEN, 0.2)

        for t in range(self.scoreTens):
            self.hw.playColour(YELLOW, 0.2)