"""Responder between Raspberry PI and PC
The module runs on native Raspberry PI environment.
Using the following command to launch the flask server:
    flask run --host=0.0.0.0
"""
import serial
from flask import Flask
from flask_socketio import SocketIO 

serialPort = serial.Serial(
    port='/dev/ttyAMA1',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('json')
def handle_json(json):
    global serialPort
    if serialPort:
        serialPort.write(json.encode())
    print('Command Received: ' + str(json))

if __name__ == "__main__":
    socketio.run(app)
