import logging


def get_logger():
    return logging.getLogger()


def stop():
    print("stop")


class Pwm:
    logger = get_logger()

    def start(self, pin: int):
        self.logger.info("start pin " + str(pin))
