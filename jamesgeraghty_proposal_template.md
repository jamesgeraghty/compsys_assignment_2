Computer Systems Assignment 2 – Home Monitoring System

Student Name: James Geraghty Student ID: 20022946

Github repo : https://github.com/jamesgeraghty/compsys_assignment_2


Introduction
The proposed project is to develop a Home monitoring system that will be powered using a
Raspberry Pi. A Http Web API framework will be implemented to allow for cross origin
requests to be made. This will include the use of multiple infrared motion sensors that will
pick up movement and replay the message back the subscriber through an email. The motion
sensor will also trigger a camera that will record a 30 second clip, this .mp4 will also be sent
to the subscriber.

The Raspberry Pi will be accessed through a Python program. The data from the motion a
motion sensor will be published and sent to an MQTT broker. There are multiple platforms
that are available; Thingspeak and Wia.io provide a useful IoT cloud platform that may help to
analysis the data collected from the motion sensor. There is also an option to connect a
smart plug the RPI, that will turn on a hall lamp when motion is detected.
Technology, Languages and Devices

• Raspberry Pi – will be the main power supply for the project
• Passive Infrared Motion Senor – this will be connected the RPI with GPIO and will
trigger the RPI camera.
• Raspberry Pi Camera – Will record a short video clip which will be triggered by the
motion sensor.
• Web API – A HTTP Web API will be used to get at the routes that will allow clients to
connect and access data that will be encoded in the URL query string.
• IFTTT – HTTP request sent to the web server; this then triggers an email to be sent to
the account.
• IDE – the project will be primarily constructed using Python IDLE and Visual studio
Code.

