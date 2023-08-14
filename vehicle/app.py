"""Responder between Raspberry PI and PC
The module runs on native Raspberry PI environment.
Using the following command to launch the flask server:
    flask run --host=0.0.0.0
"""
import json
from flask import Flask
from flask_socketio import SocketIO

from buildhat import MotorPair, ColorSensor

app = Flask(__name__)
socketio = SocketIO(app)

pair = MotorPair('A', 'B')
dist = ColorSensor('C')

@socketio.on('json')
def handle_json(command):
    parameters = json.loads(command)
    speed = parameters["speed"]
    angle = parameters["angle"]

    if angle == 0:
        speedl = speed
        speedr = speed
    elif angle < 0:
        speedl = speed * (1+angle)
        speedr = speed
    elif angle > 0:
        speedl = speed
        speedr = (speed * (1-angle))  

    pair.start(speedl=-speedl, speedr=speedr)

if __name__ == "__main__":
    socketio.run(app)
