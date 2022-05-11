import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.OUT) 
GPIO.output(12,GPIO.HIGH) 
time.sleep(0.5) 
while(True):
    x=input("Switch ON or OFF the relay?") 
    if(x=="off" or x=="OFF"): 
        GPIO.output(12,GPIO.LOW) 
        time.sleep(0.5) 
        print("Relay is switched OFF") 
    elif(x=="on" or x=="ON"): 
        GPIO.output(12,GPIO.HIGH) 
        time.sleep(0.5) 
        print("Relay is switched ON")
