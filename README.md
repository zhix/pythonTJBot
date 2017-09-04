# pythonTJBot

Goal: To run IBM TJBot using Python (instead of node.js) on Raspberry Pi.

## Preparation of environment

1) Update your Raspberry Pi via 

```sudo apt-get update```

```sudo apt-get upgrade```


2) Install **Watson Developer Cloud Python SDK** on your Raspberry Pi: https://github.com/watson-developer-cloud/python-sdk

3) Testing USB Microphone 

```sudo apt-get install portaudio19-dev python-all-dev python-pyaudio python3-pyaudio```

- Run the following tests to check if your USB mic is capable of recording in Python. 

```sudo python test_micRecord.py```

- Use an earphone/headphone to listen to your recording by ```omxplayer output.wav```.

- If it returns error, please run ```sudo python test_micStream.py``` to determine the number of channels available, and the index of the input device. Update the ```record.py``` when the information is obtained. For further documentation please refer here: https://people.csail.mit.edu/hubert/pyaudio/

4) Testing the GPIO 

- Prepare the electronics as shown in the diagram below. 
- Run the ```test_gpio.py``` script to find if every electronic is responding accordingly. 


5) Testing the Watson API

- Login to your Bluemix account to obtain the credentials. 
- edit the credentials in ```test_speechToText.py```  
- run ```test_speechToText.py``` with Python 

```test_speechToText.py```  runs the Watson's Speech-to-text function with ```output.wav``` from earlier then print output on screen. 

### Finally let's run the real thing 



