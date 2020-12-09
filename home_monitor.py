#! /usr/bin/python

# Imports
import RPi.GPIO as GPIO
import time
import requests
import os
from picamera import PiCamera
from signal import pause
import datetime
import storeFileFB
from subprocess import call 

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
	print("Waiting for PIR to settle ...")
       	
	# Loop until PIR output is 0
	while GPIO.input(pinpir) == 1:
	
		currentstate = 0

	print("    Ready")
	
	# Loop until users quits with CTRL-C
	while True:
	
		# Read PIR state
		currentstate = GPIO.input(pinpir)

		# If the PIR is triggered
		if currentstate == 1 and previousstate == 0:
		
			print("Motion detected!")
			
			#  IFTTT URL with event name, key and json parameters to trigger smart plug (values)
			r = requests.post('https://maker.ifttt.com/trigger/motion_detected/with/key/dIpYgD3DMuLS4HrXYwadC4', params={"value1":"none","value2":"none","value3":"none"})
			
			# Record new previous state
			previousstate = 1
			
			#Wait 120 seconds before looping again
			print("Waiting 5 seconds")
			time.sleep(5)
                     
			camera.rotation = 180 
			command = "MP4Box -add alert_video.h264 alert_video.mp4"
			camera.start_recording('alert_video.h264')
			camera.wait_recording(5)
			camera.stop_recording()			
			command = "MP4Box -add alert_video.h264 alert_video.mp4"
			call([command], shell=True)

			print("video converted")

			fileLoc = f'/home/pi/assignment2/compsys_assignment_2/video.mp4/frame{frame}.jpg' # set location o$
			currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

			camera.capture(fileLoc) # capture image and store in fileLoc
			print(f'frame {frame} taken at {currentTime}') # print frame number to con$
			storeFileFB.store_file(fileLoc)
			storeFileFB.push_db(fileLoc, currentTime)
			frame += 1
	
		# If the PIR has returned to ready state
		elif currentstate == 0 and previousstate == 1:
		
			print("Ready")
			previousstate = 0

		# Wait for 10 milliseconds
		time.sleep(0.01)

except KeyboardInterrupt:
	print("    Quit")

	# Reset GPIO settings
	GPIO.cleanup()
