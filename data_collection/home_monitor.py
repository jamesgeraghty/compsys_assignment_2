#! /usr/bin/python3
# James Geraghty - 20022946 Compsys Assignment 2 

# Imports
import RPi.GPIO as GPIO
import time
import requests
import os
from picamera import PiCamera
from signal import pause
import datetime
import storeFileFB

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)

# Turn off GPIO warnings
GPIO.setwarnings(False)

# Set a variable to hold the GPIO Pin identity
pinpir = 17

camera = PiCamera()

# Set GPIO pin as input
GPIO.setup(pinpir, GPIO.IN)

# Variables to hold the current and last states
currentstate = 0
previousstate = 0
camera.start_preview()
frame = 1

try:
	print("Waiting for motion sensor to get ready ...")
       	
	# Loop until PIR output is 0
	while GPIO.input(pinpir) == 1:
	
		currentstate = 0

	print("    Ready")
	
	# Loops until the program is cancelled
	while True:
	
		# Read PIR state
		currentstate = GPIO.input(pinpir)

		# If the PIR is triggered
		if currentstate == 1 and previousstate == 0:
		
			print("Motion detected!")
			
			# IFTTT webhook URL
			r = requests.post('https://maker.ifttt.com/trigger/motion_detected/with/key/dhEW-AaaxrgTc5xQdZhgqA', params={"value1":"none","value2":"none","value3":"none"})
			
			# Record new previous state
			previousstate = 1
			
			#Wait 120 seconds before looping again
			print("Waiting 10 seconds")
			time.sleep(10)
                     
			camera.rotation = 180 
                       #coverting video from .h264 to .mp4
			command = "MP4Box -add alert_video.h264 alert_video.mp4"
			camera.start_recording('alert_video.h264')
			camera.wait_recording(2)
			camera.stop_recording()			
			print("video converted")

			fileLoc = f'/home/pi/assignment2/img/frame{frame}.jpg' # set location o$
			currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	
			camera.capture(fileLoc) # capture image and store in fileLoc
			print(f'frame {frame} taken at {currentTime}') # print frame number to con$
			storeFileFB.store_file(fileLoc)
			storeFileFB.push_db(fileLoc, currentTime)
			frame += 1
	
		# If the PIR motion is returned to ready
		elif currentstate == 0 and previousstate == 1:
		
			print("Ready")
			previousstate = 0

		# Wait for 10 milliseconds
		time.sleep(0.01)

except KeyboardInterrupt:
	print("    Quit")

	# Reset GPIO settings
	GPIO.cleanup()
