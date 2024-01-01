import unittest
import led_rgb.tests.context
from led_rgb.src.led_pwm import LedPwm


class TestStringMethods(unittest.TestCase):

    def test_output(self):
        subject = LedPwm()
        self.assertEqual('0x000000', subject.get_rgb())


if __name__ == '__main__':
    unittest.main()
