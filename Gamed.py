from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

red = (130,0,0)
green = (0,0,120)

while True:
    # take reading from the all three sensors
    temp = sense.get_temperature()
    press = sense.get_pressure()
    hum = sense.get_humidity()
    
    # round hte values to one decimal place
    temp = round(temp,1)
    press = round(press,1)
    hum = round(hum,1)
    
    # create temp message
    message = "Temp: " + str(temp) 
    
    if temp > 18 and temp < 27:
        bg = green
    else:
        bg = red
    
    
    # Display temp message
    sense.show_message(message, scroll_speed = 0.050, back_colour = bg)
    
     # create pressure message
    message = "Pressure: " + str(press)
    
    if press > 979 and temp < 1027:
        bg = green
    else:
        bg = red
    
    
    # Display message
    sense.show_message(message, scroll_speed = 0.050, back_colour = bg)
    
     # create Humidity message
    message = "Humidity: " + str(hum) 
    if temp > 55 and temp < 65:
        bg = green
    else:
        bg = red
    
    
    # Display message
    sense.show_message(message, scroll_speed = 0.050, back_colour = bg)