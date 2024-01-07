#!/usr/bin/env python3

from api import Api


def start_api():
    api = Api()
    api.app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    start_api()
