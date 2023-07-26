"""Controller for SPIKE Prime
The module runs on Raspberry PI MicroPython environment.
Using the following command to run the file:
    python pyboard.py --device /dev/ttyACM0 controller.py
"""
import json
import hub,utime

# Raspberry Pi4 
serial = hub.port.D
serial.mode(hub.port.MODE_FULL_DUPLEX)
utime.sleep_ms(2000)
serial.baud(115200)

# Motors
left = hub.port.B.motor
right = hub.port.E.motor

left.pwm(0)
right.pwm(0)

print("SPIKE Prime Started!")

while True : 
    try : 
        # Read communcition from Raspberry Pi and Decode
        raw = serial.read(1000)
        
        speed = 0
        angle = 0
        if len(raw) != 0:
            raw = str(raw.decode("UTF-8"))
            parameters = json.loads(raw)
            speed = parameters["speed"]
            angle = parameters["angle"]
        
        if angle == 0:
            left.pwm(speed)
            right.pwm(-speed)
        elif angle < 0:
            left.pwm(speed * (1+angle))
            right.pwm(-speed)
        elif angle > 0:
            left.pwm(speed)
            right.pwm(-(speed * (1-angle)))      
    except: 
        pass

    utime.sleep_ms(200)
