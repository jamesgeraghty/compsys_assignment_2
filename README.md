
 ## Read Me
James Geraghty 20022946 - Computer Systems Assignment 2
---
> **Description**
---
A home monitoring system that allows the user to track various data metrics acorss a number of platforms. A Raspberry PI  model 3B is powering all the programs.

 This information is then used to trigger some smart home device.  The data can be viewed in one place through a HTML page. There are a total of three programmes runnning at once. The first program detects motion using a PIR motion sensor attached to a camera, when motion is detected it the





> **IOT Platforms Used**
---
Thingspeak is used to handle the data collected from the sense hat. Temperature, humidity and pressure data is collected. This data is then displayed on a HTML page in a graph.

The WIA platform is used to display data collected from the Raspberry Pi and sense hat. A widget is displays the data, this is then published on the HTML page. The data collected is saved in json file. This is then downloaded and import to a MongoDB, various querys can be used to get make a more details analysis of the  data collected. A HTTP request triggers 

FireBase is used to store the images saved from the motion sensor.

IFTTT is used to create webhooks that allows the data collected from the Raspberry Pi to trigger various smart home devices. When a 
