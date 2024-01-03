try:
    import RPi.GPIO as GPIO
except ImportError:
    import backend.tests.MOCK_GPIO as GPIO
import logging


def get_logger():
    return logging.getLogger()


"""
convert int in Range 0..255 to hex without leading "0x"
"""


def duty_cycle_to_hex(dc: int):
    multiplier = 256 / 100
    hex_value = hex(int(multiplier * dc)).replace("0x", "")
    return hex_value if (len(str(hex_value)) < 3) else "FF"


class LedPwm:
    rgb_current = "000000"
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

    def __init__(self, pwm_pin_red=12, pwm_pin_blue=13, pwm_pin_green=18, frequency=50):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        self.PWM_PIN_RED = pwm_pin_red
        self.PWM_PIN_BLUE = pwm_pin_blue
        self.PWM_PIN_GREEN = pwm_pin_green

        GPIO.setup(self.PWM_PIN_RED, GPIO.OUT)
        self.gpio_red = GPIO.PWM(self.PWM_PIN_RED, frequency)

        GPIO.setup(self.PWM_PIN_BLUE, GPIO.OUT)
        self.gpio_blue = GPIO.PWM(self.PWM_PIN_BLUE, frequency)

        GPIO.setup(self.PWM_PIN_GREEN, GPIO.OUT)
        self.gpio_green = GPIO.PWM(self.PWM_PIN_GREEN, frequency)

    """
    Set RGB values use percentage 0-100
    """

    def set_rgb(self, rgb: str):
        self.rgb_current = rgb
        self.logger.debug(f'set rgb {rgb}')
        self.value_red = int("0x" + rgb[0:2], 16) % self.PWM_MODULO
        self.value_blue = int("0x" + rgb[2:4], 16) % self.PWM_MODULO
        self.value_green = int("0x" + rgb[4:6], 16) % self.PWM_MODULO
        self.logger.debug(f'SELF red={self.value_red}, blue={self.value_blue} and green={self.value_green}')
        self.gpio_red.start(self.value_red)
        self.gpio_blue.start(self.value_blue)
        self.gpio_green.start(self.value_green)

    """
    get approx RGB-values that are currently mapped to the gpio pins with leading "0x"
    """

    def get_rgb(self) -> str:
        return str(self.rgb_current)

    """
    increase all colors by value
    """

    def increase_all_by(self, value: int):
        self.value_red = (self.value_red + value) % self.PWM_MODULO
        self.value_blue = (self.value_blue + value) % self.PWM_MODULO
        self.value_green = (self.value_green + value) % self.PWM_MODULO

    def cleanup(self):
        self.gpio_red.stop()
        self.gpio_blue.stop()
        self.gpio_green.stop()
        GPIO.cleanup()
