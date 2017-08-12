import pyaudio
import wave

p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
	dev=p.get_device_info_by_index(i)
	print((i,dev['name'],dev['maxInputChannels']))	##first index = INPUT DEVICE INDEX, last index = number of channels
	print(p.get_device_info_by_index(i))			##check the defaultSampleRate

stream = p.open(format=pyaudio.paInt16, 
				input_device_index=2, 
				channels=1, 
				rate=44100, 
				input=True, 
				output=False, 
				frames_per_buffer=1024)
