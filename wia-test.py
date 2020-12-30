#!/usr/bin/python3
from wia import Wia
from sense_hat import SenseHat
import  time
import requests

sense = SenseHat()
sense.clear()
wia = Wia()
wia.access_token = "d_sk_256g88JjwMoHJwHKreawliex"
#temp = sense.get_temperature()
while True:
   temp=round(sense.get_temperature(),2)
   time.sleep(900)
   wia.Event.publish(name="Temperature Update", data=temp)
   print(temp)
   r = requests.post('https://maker.ifttt.com/trigger/Too_Cold/with/key/dIpYgD3DMuLS4HrXYwadC4', params={"value1":"none","value2":"none","value3":"none"})
