from machine import Pin
from time import sleep

buttonGreen = Pin(17, Pin.IN)
buttonYellow = Pin(19, Pin.IN)
buttonBlue = Pin(22, Pin.IN)
buttonRed = Pin(27, Pin.IN)

while True:
    
    if buttonGreen.value() == True:
        print("Green pressed")
        sleep(1)
        
    elif buttonBlue.value() == True:
        print("Blue pressed")
        sleep(1)
        
    elif buttonRed.value() == True:
        print("Red pressed")
        sleep(1)
        
    elif buttonYellow.value() == True:
        print("Yellow pressed")
        sleep(1)