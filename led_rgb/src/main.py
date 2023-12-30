from led_pwm import LedPwm
from flask import Flask, make_response
from flask_cors import CORS, cross_origin
import sys
import logging

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

led = any

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


@app.route('/rgb/<rgb>')
@cross_origin()
def process_rgb(rgb):
    while len(rgb) < 6:
        rgb = "0" + rgb

    parameter_string = f'given rgb={rgb}'

    try:
        logger.debug(parameter_string)
        led.set_rgb(rgb=rgb)
        response = make_response("sucess: " + parameter_string)
        response.status_code = 200
        return response
    except:
        response = make_response("Error processing: " + parameter_string)
        response.status_code = 400
        return response


@app.route('/rgb')
@cross_origin()
def get_rgb():
    response = make_response(led.get_rgb())
    response.status_code = 200
    return response


if __name__ == "__main__":
    led = LedPwm()
    led.set_rgb("000000")

    app.run(host='0.0.0.0', port=8080)
