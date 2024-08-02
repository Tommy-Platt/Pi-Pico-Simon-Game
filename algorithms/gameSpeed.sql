BEGIN gameSpeed ()

    level = 1
    speed = ((-0.5 * level) + 2)
    sequenceLength = level + 1
    
    IF sequenceLength < 9:
        level = 1
    ELIF sequenceLength >= 10:
        level = 2
    ELIF sequenceLength > 24:
        level = 3
    
END