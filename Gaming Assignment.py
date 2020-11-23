from sense_hat import SenseHat

sense = SenseHat()

# Set up colours as variables
red = (255,0,0)
aqua = (0,90,80)
white = (255,255,255)
lightred = (100,0,60)

while True:
                sense.clear() # clear arguments
                temp = round(sense.get_temperature())
                # Prepare message to be displayed on LED Matrix
                message = 'Temperature is %d degrees celsius' %(temp)
                print(message)  # displays temperature to console for testing
                sense.set_rotation(180) # Rotate screen by 180 degrees
                # Scrolls a text message from right to left across the LED matrix
                sense.show_message(message,scroll_speed=0.10, text_colour=lightred, back_colour=aqua)