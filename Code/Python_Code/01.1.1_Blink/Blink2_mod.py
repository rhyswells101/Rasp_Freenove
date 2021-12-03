#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/26
########################################################################
from gpiozero import LED
from time import sleep

print ('Program is starting ... ')

led = LED(17)           # define LED pin according to BCM Numbering
# led = LED("J8:11")     # BOARD Numbering
'''
# pins numbering, the following lines are all equivalent
led = LED("GPIO17")     # BCM
led = LED("BCM17")      # BCM
led = LED("BOARD11")    # BOARD
led = LED("WPI0")       # WiringPi
led = LED("J8:11")      # BOARD
'''

while True:
    for i in range(1,5):
        led.on()
        r = i / 5
        print (f"led turned on for {r} secs>>>")  # print message on terminal
        sleep(r)
        led.off()
        print (f"led turned off for {r} secs>>>")  # print message on terminal
        sleep(r)
    sleep(3)
