#!/usr/bin/python3

from gpiozero import LED
from gpiozero import Servo
from time import sleep

redLed = LED(17)				#gpio17 bcm_pin11
blueLed = LED(27)				#gpio27 bcm_pin13
greenLed = LED(22)				#gpio22 bcm_pin15

servoMotor = Servo(7) 			#gpio7 bcm_pin26

textDecoded = "red blue green shake"

if "red" in textDecoded:
	print("found 'red' in text!")
	redLed.on()
	blueLed.off()
	greenLed.off()
	sleep(0.5)
	
if "blue" in textDecoded:
	print("found 'blue' in text!")
	redLed.off()
	blueLed.on()
	greenLed.off()
	sleep(0.5)
	
if "green" in textDecoded:
	print("found 'green' in text!")
	redLed.off()
	blueLed.off()
	greenLed.on()
	sleep(0.5)

if "shake" in textDecoded or "wave" in textDecoded:
	print("found 'shake' or 'wave' in text!")
	servoMotor.min()
	sleep(0.5)
	servoMotor.max()
	sleep(0.5)
	servoMotor.min()
	sleep(0.5)
	
