from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# define colours
B = (102,51,0)
b = (0,0,255)
S = (205,133,63)
W = (25,255,255)

# setup matrix variable
image_pixels = [
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,b,b,g,g,b,b,g,
    g,b,b,g,g,b,b,g,
    g,g,g,b,b,g,g,g,
    g,g,g,b,b,g,g,g,
    g,g,g,b,b,g,g,g,
    g,g,b,g,g,b,g,g,
    ]
sense.set_pixels(image_pixels)