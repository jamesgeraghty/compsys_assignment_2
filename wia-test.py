from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
green = (0, 255, 0)
red = (255,0,0)
while True:
  temp = sense.get_temperature()
  if temp >=25:
    sense.show_message("HOT!", text_colour = red)
  else:
    sense.show_message("Fine!", text_colour = green)
  print(temp)
