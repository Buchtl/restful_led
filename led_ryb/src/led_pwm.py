import RPi.GPIO as gpio
import logging

def get_logger():
    return logging.getLogger()

class LedPwm:
    gpio_red: any
    gpio_yellow: any
    gpio_blue: any
    value_red = 0
    value_yellow = 0
    value_blue = 0
    PWM_PIN_RED = 12
    PWM_PIN_YELLOW = 13
    PWM_PIN_BLUE = 18
    PWM_MODULO = 101
    logger = get_logger()

    def __init__(self):
        gpio.setwarnings(False)
        gpio.cleanup()
        frequenzy = 50
        gpio.setmode(gpio.BCM)
        
        gpio.setup(self.PWM_PIN_RED, gpio.OUT)
        self.gpio_red = gpio.PWM(self.PWM_PIN_RED, frequenzy)

        gpio.setup(self.PWM_PIN_YELLOW, gpio.OUT)
        self.gpio_yellow = gpio.PWM(self.PWM_PIN_YELLOW, frequenzy)

        gpio.setup(self.PWM_PIN_BLUE, gpio.OUT)
        self.gpio_blue = gpio.PWM(self.PWM_PIN_BLUE, frequenzy)

    """
    Set RYB values use percentage 0-100
    """
    def set_ryb(self, red: int, yellow: int, blue: int):
        self.logger.debug(f'set ryb red={red}, yellow={yellow} and blue={blue}')
        self.value_red = red % self.PWM_MODULO
        self.value_yellow = yellow % self.PWM_MODULO
        self.value_blue = blue % self.PWM_MODULO
        self.logger.debug(f'SELF red={self.value_red}, yellow={self.value_yellow} and blue={self.value_blue}')
        self.gpio_red.start(self.value_red)
        self.gpio_yellow.start(self.value_yellow)
        self.gpio_blue.start(self.value_blue)
    
    """
    increase all colors by value
    """
    def increase_all_by(self, value: int):
        self.value_red = (self.value_red + value) % self.PWM_MODULO
        self.value_yellow = (self.value_yellow + value) % self.PWM_MODULO
        self.value_blue = (self.value_blue + value) % self.PWM_MODULO
        self.set_ryb(red=self.value_red, yellow=self.value_yellow, blue=self.value_blue)
    
    def cleanup(self):
        self.gpio_red.stop()
        self.gpio_yellow.stop()
        self.gpio_blue.stop()
        gpio.cleanup()