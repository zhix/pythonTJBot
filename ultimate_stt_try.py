#!/usr/bin/python3

import pyaudio
import wave

import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

from gpiozero import LED
from gpiozero import Servo
from time import sleep



CHUNK = 512					##cut down the size
FORMAT = pyaudio.paInt16
CHANNELS = 1				##check the channel and index with stream.py
INPUT_DEVICE_INDEX=2
RATE = 44100				##check the default rate with stream.py
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

redLed = LED(17)					#gpio17 bcm_pin11
blueLed = LED(27)				#gpio27 bcm_pin13
greenLed = LED(22)				#gpio22 bcm_pin15
servoMotor = Servo(7) 			#gpio7 bcm_pin26


while True:
	## recording speech for 5 seconds

		stream = p.open(format=FORMAT,
						channels=CHANNELS,
						input_device_index=INPUT_DEVICE_INDEX,
						rate=RATE,
						input=True,
						frames_per_buffer=CHUNK)

		print("* listening")

		frames = []
		count = 0
		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)
			if i % int(RATE / CHUNK) ==0:
				count = count +1
				print("*"*count + str(RECORD_SECONDS-count))

		print("*"*count + " transcripting recording")

		stream.stop_stream()
		stream.close()
		p.terminate()

		#wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		#wf.setnchannels(CHANNELS)
		#wf.setsampwidth(p.get_sample_size(FORMAT))
		#wf.setframerate(RATE)
		#wf.writeframes(b''.join(frames))
		#wf.close()

		## speech-to-text function 
		
		speech_to_text = SpeechToTextV1(
			username='0f8e25a9-2b1e-4dc4-bb88-60fdc17409f6',
			password='4ssHZACduREg',
			x_watson_learning_opt_out=False)

		s2t = speech_to_text.recognize(frames, content_type='audio/l16', timestamps=True, word_confidence=True)
		
		with open(p,'rb') as audio_file:
			s2t = speech_to_text.recognize(audio_file, content_type='audio/l16', timestamps=True, word_confidence=True)
			textDecoded = s2t["results"][0]["alternatives"][0]["transcript"]
			print(textDecoded)
			sleep(1)
						
				
		#if "red" in textDecoded:
			#print("found 'red' in text!")
			#redLed.on()
			#blueLed.off()
			#greenLed.off()
			#sleep(0.5)
			
		#if "blue" in textDecoded:
			#print("found 'blue' in text!")
			#redLed.off()
			#blueLed.on()
			#greenLed.off()
			#sleep(0.5)
			
		#if "green" in textDecoded:
			#print("found 'green' in text!")
			#redLed.off()
			#blueLed.off()
			#greenLed.on()
			#sleep(0.5)

		#if "shake" in textDecoded or "wave" in textDecoded:
			#print("found 'shake' or 'wave' in text!")
			#servoMotor.min()
			#sleep(0.5)
			#servoMotor.max()
			#sleep(0.5)
			#servoMotor.min()
			#sleep(0.5)

