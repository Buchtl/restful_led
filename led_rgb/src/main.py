from led_pwm import LedPwm
import time

if __name__ == "__main__":
    led = LedPwm()
    led.set_red(red=1)
    time.sleep(1)
    led.set_red(red=20)
    time.sleep(1)
    led.set_red(red=40)
    time.sleep(1)
    led.set_red(red=60)
    time.sleep(1)
    led.set_red(red=80)
    time.sleep(1)
    led.set_red(red=100)
    time.sleep(1)
    led.cleanup()
