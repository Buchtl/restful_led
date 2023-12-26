from led_pwm import LedPwm
import time

if __name__ == "__main__":
    led = LedPwm()
    led.set_ryb(red=0, yellow=0, blue=0)
    time.sleep(1)
    for x in range(0,4):
        led.increase_all_by(20)
        time.sleep(1)
    led.cleanup()