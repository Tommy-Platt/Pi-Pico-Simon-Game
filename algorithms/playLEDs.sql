BEGIN playSound(note, duration)

    piezo.play(note)
    sleep(duration)
    piezo.stop()
    sleep(duration)

END

BEGIN lightLED(colour, state)

    led = GET colour.LED
    led.value(state)

END

BEGIN playColour(colour, duration)

    lightLED(colour, True)
    note = GET colour.NOTE
    playSound(note, duration)
    lightLED(colour, False)

END