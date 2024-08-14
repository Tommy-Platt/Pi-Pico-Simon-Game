BEGIN gameSpeed ()

    level = 1
    speed = ((-0.5 * level) + 2)
    sequenceLength = level + 1
    
    IF sequenceLength < 9 THEN
        level = 1
    ELSE IF sequenceLength >= 10 THEN
        level = 2
    ELSE IF sequenceLength > 24 THEN
        level = 3
    
    END IF

END