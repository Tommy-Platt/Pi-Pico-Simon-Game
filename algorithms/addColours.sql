BEGIN addColours()

    randomColour = RAND(colourList)
    colourSequence.append(colour)
    speed = 1

-- Increases game speed every 5 rounds
    IF speed % 5 = 0 THEN
        
        IF speed GREATER THAN 0.1 THEN
            speed = speed - 0.1

        END IF

    END IF

END addColours()