BEGIN checkColours ()

    sequenceCorrect = True

    FOR c IN colourSequence:

        GET userColour

        IF userColour == NONE
            CALL playSimon -- Continues playing game (this function will repeat eventually)

        playColour(userColour, 0.5)
            
        IF userColour NOT IN colourSequence
            sequenceCorrect = False
            BREAK
        
END checkColours()