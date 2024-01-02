import logging
import os
import signal
import sys
import threading
import time

from flask import Flask, make_response
from flask_cors import CORS, cross_origin

from led_pwm import LedPwm


class Api:
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    led: LedPwm

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def shutdown_server(self):
        time_to_kill = 0
        self.logger.info(f"Shutting down server in {time_to_kill} seconds...")
        time.sleep(time_to_kill)
        self.logger.info(f'shutting down pid {os.getpid()}')
        os.kill(os.getpid(), signal.SIGINT)

    def __init__(self, name='flask_app', debug=True):
        self.logger.debug("init api")
        self.app = Flask(name)
        self.app.debug = debug

        # Define your routes and other Flask configurations here
        self.define_routes()
        self.led = LedPwm()

    def define_routes(self):
        @self.app.route('/rgb/<rgb>')
        @cross_origin()
        def process_rgb(rgb):
            """
            Set RGB value

            Example Request:
            GET /rgb/00FF00

            Returns:
            - HTTP Status Code: 200 OK (Data processed successfully)

            OR
            - HTTP Status Code: 200 OK (RGB set)
            - HTTP Status Code:  Internal Server Error (Error processing)
            """
            while len(rgb) < 6:
                rgb = "0" + rgb

            parameter_string = f'given rgb={rgb}'

            try:
                self.logger.debug(parameter_string)
                self.led.set_rgb(rgb=rgb)
                response = make_response(self.led.get_rgb())
                response.status_code = 200
                return response
            except:
                response = make_response("Error processing: " + parameter_string)
                response.status_code = 500
                return response

        @self.app.route('/rgb')
        @cross_origin()
        def get_rgb():
            """
            Get current RGB value

            Example Request:
            GET /rgb

            Returns:
            - HTTP Status Code: 200 OK (RGB set)
            - Plain Text: "000000"
            """
            response = make_response(self.led.get_rgb())
            response.status_code = 200
            return response

        @self.app.route('/shutdown')
        def shutdown_server():
            shutdown_thread = threading.Thread(target=self.shutdown_server)
            shutdown_thread.start()
            return 'Shutting down...'
