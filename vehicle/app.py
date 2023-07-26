"""Responder between Raspberry PI and PC
The module runs on native Raspberry PI environment.
Using the following command to launch the flask server:
    flask run --host=0.0.0.0
"""
import cv2
import serial
import socketio 
from flask import Flask, Response, request 

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cam.set(cv2.CAP_PROP_FPS, 20)

serialPort = serial.Serial(
    port='/dev/ttyAMA1',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def gen_frames():
    while True:
        success, frame = cam.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
            )

app = Flask(__name__)
sio = socketio.Server()

@sio.on('connect')
def connect(sid, environ):
    print('Connected')

@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/cmd", methods=["POST"])
def cmd():
    global serialPort
    if serialPort:
        serialPort.write(request.json.encode())
    return "Success!"
 
if __name__ == "__main__":
    app.run(debug=True)
