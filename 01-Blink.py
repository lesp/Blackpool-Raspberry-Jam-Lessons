from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    
#Can you make two LEDs flash...

#Together so that both LEDs turn on, off at once.
#Alternating, so that one LED turns on, the other turns off.