#!/usr/bin/python3
from wia import Wia
from sense_hat import SenseHat
import  time

sense = SenseHat()
sense.clear()
wia = Wia()
wia.access_token = "d_sk_256g88JjwMoHJwHKreawliex"
#temp = sense.get_temperature()
while True:
   temp=round(sense.get_temperature(),2)
   time.sleep(10)
   wia.Event.publish(name="Temperature Update", data=temp)
   print(temp)

