import RPi.GPIO as GPIO

class Heater():
    def __init__(self, PIN):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)
        GPIO.output(PIN, GPIO.HIGH)
        self.current = GPIO.HIGH
        
    def on(self):
        if self.current == GPIO.LOW:
            return
       
        GPIO.output(PIN, GPIO.LOW)
        self.current = GPIO.LOW

    def off(self):
        if self.current == GPIO.HIGH:
            return
        
        GPIO.output(PIN, GPIO.HIGH)
        self.current = GPIO.HIGH
       
    def shutdown(self):
        GPIO.cleanup()