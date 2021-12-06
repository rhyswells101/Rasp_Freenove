#!/usr/bin/env python3
########################################################################
# Filename    : ButtonLED.py
# Description : Control led with button.
# Author      : www.freenove.com
# modification: 2019/12/27
########################################################################
from gpiozero import LED, Button
from signal import pause
from time import sleep
from Mods.mod1 import wait

print ('Program is starting ... ')

led = LED(17)       # define LED pin according to BCM Numbering
button = Button(18) # define Button pin according to BCM Numbering

def onButtonPressed(): 
    led.on()
    print("Button is pressed, led turned on >>>")
    print("We now wait 2 seconds")
    wait()
    
    
def onButtonReleased():
    led.off()
    print("Button is released, led turned on <<<")

button.when_pressed = onButtonPressed
button.when_released = onButtonReleased

pause()

