from sense_hat import SenseHat
import time

sh = SenseHat()
sh.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def s():
    G = green
    O = nothing
    logo = [
    O, O, O, O, G, G, O, O,
    O, O, O, G, G, O, O, O,
    O, O, G, G, O, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, O, O, G, G, O, O,
    O, O, O, O, O, G, G, O,
    O, O, O, O, G, G, O, O,
    O, O, O, G, G, O, O, O,
    ]
    return logo

def r():
    G = green
    R = red
    O = nothing
    logo = [
    O, O, O, R, R, R, R, R,
    O, O, O, R, R, O, R, R,
    O, O, O, R, R, O, R, R,
    O, O, O, R, R, O, R, R,
    O, O, O, R, R, R, R, O,
    O, O, O, R, R, R, R, R,
    O, O, O, R, R, O, R, R,
    O, O, O, R, R, O, R, R,
    ]
    return logo

def m():
    W = green
    O = nothing
    logo = [
    O, W, W, W, O, O, W, W,
    O, W, W, W, W, W, W, W,
    O, W, W, W, W, W, W, W,
    O, W, W, O, W, O, W, W,
    O, W, W, O, O, O, W, W,
    O, W, W, O, O, O, W, W,
    O, W, W, O, O, O, W, W,
    O, W, W, O, O, O, W, W,
    ]
    return logo

images = [s, r, m]
count = 0

while True: 
    sh.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
