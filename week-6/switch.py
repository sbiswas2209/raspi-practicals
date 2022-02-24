import RPi.GPIO as GPIO
import time

led = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.IN)
GPIO.setup(40, GPIO.OUT)

while True:
    time.sleep(1)

    if GPIO.input(led) == GPIO.HIGH:
        GPIO.output(40, GPIO.HIGH)
        print("Pin is in on condition")
        
    else:
        GPIO.output(40, GPIO.LOW)
        print("Pin is in off condition")
GPIO.cleanup()