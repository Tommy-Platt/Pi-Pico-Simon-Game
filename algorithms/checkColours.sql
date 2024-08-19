BEGIN checkColours ()

        FOR c IN colourSequence:
            IF userColour == NONE
                CALL playSimon

            playColour(note, duration, led)
            
            IF userSequence NOT IN colourSequence
                sequenceCorrect = False
                BREAK
        
END checkColours()
