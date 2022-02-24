import RPi.GPIO as GPIO  
import time  
led = 40
GPIO.setmode( GPIO.BOARD)  
GPIO.setup( led, GPIO.OUT)  
pwm_led = GPIO.PWM( led, 50)  
pwm_led.start(100)  
duty=0
while True:  
    if duty<100:
        duty+=25
    else:
        duty-=25
    pwm_led.ChangeDutyCycle(duty)  
    time.sleep(0.5)  
GPIO.cleanup()