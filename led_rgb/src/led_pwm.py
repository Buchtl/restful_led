import RPi.GPIO as gpio
import logging


def get_logger():
    return logging.getLogger()


class LedPwm:
    gpio_red: any
    gpio_blue: any
    gpio_green: any
    value_red = 0
    value_blue = 0
    value_green = 0
    PWM_PIN_RED = 12
    PWM_PIN_BLUE = 13
    PWM_PIN_GREEN = 18
    PWM_MODULO = 101
    logger = get_logger()

    def __init__(self):
        gpio.setwarnings(False)
        gpio.cleanup()
        frequenzy = 50
        gpio.setmode(gpio.BCM)

        gpio.setup(self.PWM_PIN_RED, gpio.OUT)
        self.gpio_red = gpio.PWM(self.PWM_PIN_RED, frequenzy)

        gpio.setup(self.PWM_PIN_BLUE, gpio.OUT)
        self.gpio_blue = gpio.PWM(self.PWM_PIN_BLUE, frequenzy)

        gpio.setup(self.PWM_PIN_GREEN, gpio.OUT)
        self.gpio_green = gpio.PWM(self.PWM_PIN_GREEN, frequenzy)

    """
    Set RYB values use percentage 0-100
    """

    #def set_ryb(self, red: int, blue: int, green: int):
    #    self.logger.debug(f'set ryb red={red}, yellow={yellow} and blue={blue}')
    #    self.value_red = red % self.PWM_MODULO
    #    self.value_blue = blue % self.PWM_MODULO
    #    self.value_green = green % self.PWM_MODULO
    #    self.logger.debug(f'SELF red={self.value_red}, blue={self.value_blue} and green={self.value_green}')
    #    self.gpio_red.start(self.value_red)
    #    self.gpio_yellow.start(self.value_blue)
    #    self.gpio_blue.start(self.value_green)

    """
    Set RGB values use percentage 0-100
    """

    def set_rgb(self, rgb: str):
        v = "0x" + rgb[0:2]
        self.logger.debug(f'set rgb {rgb} and {v}')
        self.value_red = int("0x" + rgb[0:2], 16) % self.PWM_MODULO
        self.value_blue = int("0x" + rgb[2:4], 16) % self.PWM_MODULO
        self.value_green = int("0x" + rgb[4:6], 16) % self.PWM_MODULO
        self.logger.debug(f'SELF red={self.value_red}, blue={self.value_blue} and green={self.value_green}')
        self.gpio_red.start(self.value_red)
        self.gpio_blue.start(self.value_blue)
        self.gpio_green.start(self.value_green)

    """
    increase all colors by value
    """

    def increase_all_by(self, value: int):
        self.value_red = (self.value_red + value) % self.PWM_MODULO
        self.value_blue= (self.value_blue + value) % self.PWM_MODULO
        self.value_green = (self.value_green + value) % self.PWM_MODULO
        self.set_ryb(red=self.value_red, blue=self.value_blue, green=self.value_green)

    def cleanup(self):
        self.gpio_red.stop()
        self.gpio_blue.stop()
        self.gpio_green.stop()
        gpio.cleanup()
