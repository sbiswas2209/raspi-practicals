import time
import RPi.GPIO as gpio
pin_1 = 3
pin_2 = 5
output_1 = 7
output_2 = 11
gpio.setmode(gpio.BOARD)
gpio.setup(pin_1, gpio.IN, pull_up_down=gpio.PUD_UP, initial=0)
gpio.setup(pin_2, gpio.IN, pull_up_down=gpio.PUD_UP, initial=1)
gpio.setup(output_1, gpio.OUT)
gpio.setup(output_2, gpio.OUT)
def rising():
    print("Low -> High")
def falling():
    print("High -> Low")
while True:
    if gpio.input(pin_1) == False:
        time.sleep(0.1)
        if gpio.input(pin_1) == True:
            rising()
            gpio.output(output_1, gpio.HIGH)
            time.sleep(2)
            gpio.output(output_2, gpio.LOW)
        else:
            pass
    if gpio.input(pin_2) == True:
        time.sleep(0.1)
        if gpio.input(pin_2) == False:
            falling()
            gpio.output(output_2, gpio.HIGH)
            time.sleep(2)
            gpio.output(output_1, gpio.LOW)
        else:
            pass
    time.sleep(0.1)