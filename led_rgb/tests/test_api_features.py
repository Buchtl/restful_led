import subprocess
import threading
import time
import unittest

import requests


class TestStringMethods(unittest.TestCase):
    thread_api: threading.Thread
    URL_BASE = "http://localhost:8080"
    URL_RGB = URL_BASE + "/rgb"
    URL_SHUTDOWN = URL_BASE + "/shutdown"
    process: subprocess.Popen

    def setUp(self):
        cwd = "../../"
        cmd = "./run.sh"
        self.process = subprocess.Popen(cmd, cwd=cwd)
        # give server time to start
        time.sleep(3)

    def tearDown(self):
        requests.get(self.URL_SHUTDOWN)
        self.process.wait()

    def test_current_rgb(self):
        actual = requests.get(self.URL_RGB).text
        self.assertEqual('0x000000', actual)


if __name__ == '__main__':
    unittest.main()
