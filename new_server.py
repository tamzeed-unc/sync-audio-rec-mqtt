#
'''
Script to automate synchronous audio data collection using MQTT.

Tested on Mac OS 10.13.4 as the server and Raspberry Pi as the client.

1) Install MQTT server on the Mac https://simplifiedthinking.co.uk/2015/10/03/install-mqtt-server/
2) Install paho-mqtt python package `pip install paho-mqtt` on the server and the client.

'''

import paho.mqtt.publish as publish
import subprocess
import time
import os
import sounddevice as sd
import soundfile as sf
import sys


DATA_DIR = "/tmp/speech_commands/"
record_list = "speech_commands_playlist.txt"
sleep_duration = 1
start_from = 0 #Parameter to skip recording some audio files, e.g., in the case of resuming the recordings.

i = 0
# with open(DATA_DIR + record_list, "r") as file:
# 	for line in file:
# 		if i < start_from:
# 			i = i + 1
# 			continue
# 		publish.single("filenames", line.rstrip(), hostname="localhost")
# 		filename, _ = line.split(',')
# 		subprocess.call(["afplay", DATA_DIR + filename])

# 		# Sleep for a few milliseconds to let the recording finish on the RPI
# 		time.sleep(sleep_duration)
# 		i = i + 1
directory='dataset/'

# for filename in os.listdir(directory):
#     if filename.endswith(".wav") : 
#         print (filename)
publish.single("filenames", sys.argv[1], hostname="localhost")
        # subprocess.call(["afplay", directory + filename])
