from led_pwm import LedPwm
import time
from flask import Flask, request, make_response
import sys
import logging

app = Flask(__name__)

led = any

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/ryb')
def process_ryb():
    red = request.args.get('red', "0")
    yellow = request.args.get('yellow', "0")
    blue = request.args.get('blue', "0")

    parameter_string = (f'given red={red}, yellow={yellow} and blue={blue}')

    try:
        logger.debug(parameter_string)
        led.set_ryb(red = int(red), yellow = int(yellow), blue=int(blue))
        response = make_response("sucess: " + parameter_string)
        response.status_code = 200
        return response
    except:
        response = make_response("Error processing: " + parameter_string)
        response.status_code = 400
        return response

if __name__ == "__main__":
    led = LedPwm()
    led.set_ryb(red=0, yellow=0, blue=0)
    #time.sleep(1)
    #for x in range(0,4):
    #    led.increase_all_by(20)
    #    time.sleep(1)
    #led.cleanup()

    app.run(host='0.0.0.0', port=8080)