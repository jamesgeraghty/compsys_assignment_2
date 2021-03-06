## Read Me
James Geraghty 20022946 - Computer Systems Assignment 2

---

> **Description**
---
This is a home monitoring system that allows the user to track various data metrics across a number of IoT platforms. A Raspberry PI model 3B is powering all the programs. Using a number of API's to make the programme work, this systems allows the user to monitor and keep track of their home from anywhere in the world.

This information is then used to trigger some smart home device.  The data can be viewed in one place through a HTML page. This page is hosted on a web server that was setup on the Raspberry Pi.  There are a total of three programmes running at once. The first program detects motion using a PIR motion sensor attached to a camera. When motion is detected it triggers a webhook that is linked to a smart home bulb, at the same time an image is capture using the raspberry Pi Camera and sent the Firebase database.

The second programme is recording room data. Room humidity, pressure and temperature  are being recorded and displayed on a graph that is viewed on the webpage. When the temperature dips below 20 degrees a second webhook triggers a smart plug that is connected to a radiator in the room. 

The third program displays the temperature of the room. This is recorded every 15 minutes and is displayed on a widget. The temperature data is recorded in JSON format and be stored and queried using MongoDB.

A live web cam server is also connected to the Raspberry Pi, they allow the user to see a live video picture from the outside of the house. 

![](images/collage.jpg)

<p>&nbsp;</p>


>**Programming Languages Used**
---
- Python - Due to its user-friendly data structures and the extensive support libraries available, Python is primarily used to write the programs for this project. 

- JavaScript - When building the cross platform app between Firebase and Glitch, JavaScript  was used to implement the link between the data and the web application. WIA MQTT API collects temperature data from through the sense hat. 

- HTML and CSS - are used to design the website that displays the information collected from the Raspberry PI.

<p>&nbsp;</p>


>**Physical Devices**
---
- Raspberry Pi Model 3

- Raspberry Pi Camera

- Sense Hat Black Hat Hack3r

- PIR Motion Sensor

- Micro Soft Webcam

![](images/rpi1.jpg)  ![](images/rpi2.jpg)

<p>&nbsp;</p>

> **IOT Platforms Used**
---
Thingspeak - is used to handle the data collected from the sense hat. Temperature, humidity, and pressure data is collected, and this data is then displayed on a HTML page in a graph. There are number of 'Reacts' created in Thingspeak that allows you to trigger HTTP requests when a certain condition has been met. In this case when the temperature is below 17 degrees in the room, a HTTP request triggers the smart home plug to switch on. In reverse when the temperature gets to above 25 degrees a second trigger will turn off the smart plug. A "No Data Check" react, checks to see if data has been received at least once every 60 minutes. If there is no data being recorded the subscriber will be notified through email that there may be connection issue.

![](images/thingspeak2.jpg)

The WIA platform is very user friendly and allows the user to easily and display data collected from the Raspberry Pi and sense hat through a simple Python program. A widget displays the current data in numeric form, this is then published on the HTML page. The data collected is saved in json file. This is then downloaded and import to a MongoDB, various queries can be used to get make a more detailed analysis of the data collected. A HTTP request triggers
![](images/wia.png)

IFTTT is used to create webhooks that allows the data collected from the Raspberry Pi to trigger various smart home devices. When the temperature in the room goes below 17 degrees, this causes the smart plug that is connected to a radiator to turn on. An email is also sent to the user to notify the user. When is motion is detected by the PIR motion sensor, the smart bulb is triggered. When the temperature goes above 25 the smart bulb is turned off.



![](images/applets.png)

<p>&nbsp;</p>


>**Data Storage**
---
- FireBase Realtime Database is used to store the images saved from the motion sensor program. This broker topology is used to publish the event data to Firebase. This data is stored as a JSON and then synchronised in real-time to anyone who is connected. The Firebase API makes is easy for data to accessed through a web application. The data remains available even when the application goes offline. Every time motion is detected from the PIR sensor, a photograph is taken with the Raspberry Pi camera and then it published to the Firebase database. Firebase uses websockets which are faster than HTTP requests, this that allows the server to push data to the client. The Glitch application is connected to the Firebase through web sockets. The data is then syncs through the web socket automatically and publishes the latest picture that has been taken.


![](images/firebase.png)


- MongoDD - Temperature data collected from the WIA widget is stored in the JSON format. MongoDB can store the data collected and then it can accessed at anytime. The MongoDB document format means that it can accessed from any language, in data 

![](images/mongoDB.jpg)

> **Resources**
---
* [PiHut - using IFTTT](https://thepihut.com/blogs/raspberry-pi-tutorials/using-ifttt-with-the-raspberry-pi)
* [Setting up an Apache Web Server on a Raspberry Pi](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md)
* [Publishing Events with WIA.io](https://developers.wia.io/wia-cloud/publish-an-event)
* [Build a motion detection system with a Raspberry Pi](https://opensource.com/article/20/11/motion-detection-raspberry-pi)
* [Make Raspberry Pi Webcam Server](https://www.instructables.com/How-to-Make-Raspberry-Pi-Webcam-Server-and-Stream-/)
* [Connect and control Raspberry Pi motion detector PIR](https://tutorials-raspberrypi.com/connect-and-control-raspberry-pi-motion-detector-pir/)


