import cv2
import keyboard
import requests
import time
import json
import random


while True:
    if keyboard.is_pressed("up"):
        print("You pressed 'up'.")
        parameters = {
            "angle": 0.5,
            "speed": 100
        }
        response=requests.post("http://192.168.100.22:5000/cmd", json=json.dumps(parameters))
    elif keyboard.is_pressed("left"):
        print("You pressed 'left'.")
        parameters = {
            "angle": 0.8,
            "speed": 100
        }
        response=requests.post("http://192.168.100.22:5000/cmd", json=json.dumps(parameters))
    elif keyboard.is_pressed("right"):
        print("You pressed 'right'.")
        parameters = {
            "angle": 0.2,
            "speed": 100
        }
        response=requests.post("http://192.168.100.22:5000/cmd", json=json.dumps(parameters))
    elif keyboard.is_pressed("down"):
        print("You pressed 'down'.")
        parameters = {
            "angle": 0.5,
            "speed": -100
        }
        response=requests.post("http://192.168.100.22:5000/cmd", json=json.dumps(parameters))
    elif keyboard.is_pressed("esc"):
        print("You pressed 'esc'.")
        break

    # Save camera data
    # cap = cv2.VideoCapture('http://192.168.100.22:5000/video_feed')
    # cap.grab()

    # success, frame = cap.read()
    # cv2.imwrite("{}.jpg".format(str(random.randrange(10000))), frame)

    time.sleep(0.1)

    