

import RPi.GPIO as gpio

class LedPwm:
    red: any
    yellow: any
    blue: any

    def __init__(self):
        gpio.setwarnings(False)
        frequenzy = 50
        gpio.setmode(gpio.BCM)
        gpio.setup(13, gpio.OUT)
        self.red = gpio.PWM(13, frequenzy)
        gpio.setup(14, gpio.OUT)
        gpio.output(14, gpio.LOW)
        self.yellow = gpio.PWM(14, frequenzy)
        gpio.setup(15, gpio.OUT)
        gpio.output(15, gpio.LOW)
        self.blue = gpio.PWM(15, frequenzy)

    def set_red(self, red: int):
        print("Started with value " + str(red))
        self.red.start(red)
    
    def cleanup(self):
        gpio.cleanup()