## Commands
1. Run Flask Server on Raspberry PI.
```bash
flask run --host=0.0.0.0
```
    
2. Raspberry PI controller.
```bash
python pyboard.py --device /dev/ttyACM0 controller.py
```

3. Enter MicroPython in terminal.
```bash
screen /dev/ttyACM0 115200
```

4. Terminate `screen`
```bash
pkill screen
```

## Resources
1. Remote Development using SSH  
    * https://code.visualstudio.com/docs/remote/ssh