"""Script using to retmotely control the vehicle.
"""

import time
import json
import socketio
import keyboard

sio = socketio.Client()

# Varaiable Definition
VEHICLE_IPADDRESS = "192.168.100.22"
speed = 60

@sio.event
def connect():
    print('Connected to server')

if __name__ == '__main__':
    sio.connect('http://{}:5000'.format(VEHICLE_IPADDRESS))

    while True:
        if keyboard.is_pressed("up"):
            parameters = {
                "angle": 0,
                "speed": speed
            }
            sio.emit('json', json.dumps(parameters))
            time.sleep(0.1)

        elif keyboard.is_pressed("left"):
            parameters = {
                "angle": -0.2,
                "speed": speed
            }
            sio.emit('json', json.dumps(parameters))
            time.sleep(0.1)

        elif keyboard.is_pressed("right"):
            parameters = {
                "angle": 0.2,
                "speed": speed
            }
            sio.emit('json', json.dumps(parameters))
            time.sleep(0.1)
        
        elif keyboard.is_pressed("down"):
            parameters = {
                "angle": 0,
                "speed": -speed
            }
            sio.emit('json', json.dumps(parameters))
            time.sleep(0.1)

        elif keyboard.is_pressed("esc"):
            print("Quit.")
            break
    
    sio.disconnect()
        