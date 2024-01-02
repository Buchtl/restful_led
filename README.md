# restful_led

Controlling a rgb-led that is connected to a raspberry pi by a browser application

## Pi
* RGB-LED is controlled by software pwm
* REST-API is provided via flask
* Starting backend:
  * `cd backend`
  * `python -m venv ./venv`
  * `. venv/bin/activate`
  * `pip install -r requirements.txt`
  * if on pi: `pip install -r requirements.pi.txt`
  * `./run.sh`

## Web-Frontend
* REACT-APP using TypeScript
* Starting frontend:
  * `cd frontend`
  * `npm install`
  * `npm start`
