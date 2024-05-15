import serial
import json
import time

start = time.time()
port = 'usbserial-NN' # Serial Port Here

class Board():

    def send(self, ary):
        for i in range(0, len(ary)):
            ary[i] = str(ary[i])
        inp = ','.join(ary)
        inp = inp.encode()
        # self.S.flushInput()
        # self.S.flushOutput()
        self.S.write(inp)

    def get(self):
        # self.S.flushInput()
        ser_bytes = self.S.readline()
        decoded_bytes = ser_bytes[0:-2].decode("utf-8")
        return json.loads(decoded_bytes)
    
    def __init__(self, port):
        self.S = serial.Serial('/dev/cu.' + port)
        self.S.flushInput()
        self.seg = ''

board = Board(port)
