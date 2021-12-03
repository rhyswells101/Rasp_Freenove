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

#########################################################################
#Morse code:
# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':

			# Looks up the dictionary and adds the
			# correspponding morse code
			# along with a space to separate
			# morse codes for different characters
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			# 1 space indicates different characters
			# and 2 indicates different words
			cipher += ' '

	return cipher

def main():
	message=input("Enter a word you wish to put into Morse code: ")
	# message = "GEEKS-FOR-GEEKS"
	result = encrypt(message.upper())
	print(result)

	for i in result:
		if i =="-":
			print("dash")
			led.on()
			print("Led is on >>>")
			sleep(1.5)
			led.off()
			print("Led is off >>>")
			sleep(1)
		if i ==".":
			print("dot")
			led.on()
			print("Led is on >>>")
			sleep(0.5)
			led.off()
			print("Led is off >>>")
			sleep(1)
		if i ==" ":
			print("space")
			led.off()
			print("Led is off >>>")
			sleep(2)
	return()
        
#########################################################################

while True:
    main()
    sleep(4)
    print("Did you get the word?","\n")