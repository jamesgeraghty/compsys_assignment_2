from wia import Wia
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
wia = Wia()
wia.access_token = "d_sk_256g88JjwMoHJwHKreawliex"
temp = sense.get_temperature()

wia.Event.publish(name="Temperature Update", data=temp)
