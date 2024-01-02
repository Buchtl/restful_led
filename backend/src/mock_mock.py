import logging

from mock_pwm import Pwm

logger = logging.getLogger()

BCM = 0
OUT = 0


def PWM(pin: int, frequency: int):
    logger.info(f'creating PWM on pin {pin} with frequency {frequency} ')
    return Pwm()


def cleanup():
    logger.info("cleanup")


def setwarnings(value: bool):
    logger.info(f'set warnings {value}')


def setup(pin: int, mode: int):
    logger.info(f'setup pin {pin} with mode {mode}')


def setmode(mode: int):
    logger.info(f'setmode {mode}')
