import serial
import json
import time

start = time.time()
port = 'usbmodem101' # 'usbserial-110' 

class Board():

    def send(self, ary):
        for i in range(0, len(ary)):
            ary[i] = str(ary[i])
        inp = ','.join(ary)
        inp = inp.encode()
        # self.S.flushInput()
        # self.S.flushOutput()
        self.S.write(inp)

    def get(self, seg):
        if self.number >= 40:
            self.number = 0
            self.S.flushInput()
            try:
                ser_bytes = self.S.readline()
                decoded = json.loads(ser_bytes[0:-2].decode("utf-8"))
            except:
                print("Reset & OOD.")
        else:
            ser_bytes = self.S.readline()
            decoded = json.loads(ser_bytes[0:-2].decode("utf-8"))
            self.number += 1

        if seg == 0:
            return decoded
        else:
            try:
                seg["setP"] = decoded["setP"]
            except:
                pass
            
            try:
                seg["PWM"] = decoded["PWM"]
                seg["valveState"] = decoded["valveState"]
            except:
                pass
            
            seg["chamPress"] = decoded["chamPress"]
            seg["chamPress"] = decoded["chamPress"]
            seg["boardTime"] = decoded["boardTime"]

            return seg
    
    def __init__(self, port):
        self.S = serial.Serial('/dev/cu.' + port)
        self.S.flushInput()
        self.seg = ''
        self.number = 0

board = Board(port)
