BEGIN addColours()

    colour = RAND(colourList)
    colourSequence.append(colour)
    roundLength = LENGTH(colourSequence)

-- Increases game speed every 5 rounds
    IF roundLength % 5 = 0 THEN
        
        IF pauseTime > 2 THEN
            pauseDuration = pauseDuration - 1

        END IF

    END IF

END addColours()