#!C:\Users\jedip\AppData\Local\Programs\Python\Python35\Python.exe
from main import *
class command:
    lock = multiprocessing.Lock()
    address = [b'\x61', b'\x62', b'\x63', b'\x64', b'\x65', b'\x66',
               b'\x67', b'\x68', b'\x69', b'\x6A', b'\x6B', b'\x6C',
               b'\x6D', b'\x6E', b'\x6F', b'\x70', b'\x71', b'\x72']

    mCom = [b'\x61', b'\x62', b'\x63', b'\x64', b'\x65', b'\x66',
            b'\x67', b'\x68', b'\x69', b'\x6A', b'\x6B', b'\x6C']

    sCom= [b'\x61', b'\x62', b'\x63', b'\x64', b'\x65', b'\x66',
           b'\x67', b'\x68', b'\x69', b'\x6A', b'\x6B', b'\x6C']

    def __init__(self, port, baud):
        self.port = port
        self.baud = baud
        self.ser = serial.Serial(self.port, self.baud)

    def writeSerial(self, payload):
        try:
            self.payload = payload
            self.lock.acquire()
            self.ser.write(self.payload)
            self.lock.release()
            return True
        except:
            return False

    def chLAccel(self, accel):
        self.accel = int(accel)
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[2]                                   \
                     + self.mCom[4]                                      \
                     + self.accel.to_bytes(4, byteorder = 'little')
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def chRAccel(self, accel):
        self.accel = accel
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[3]                                   \
                     + self.mCom[4]                                      \
                     + self.accel.to_bytes(4, byteorder = 'little')
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def chBAccel(self, accel):
        self.accel = accel
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[8]                                   \
                     + self.mCom[4]                                      \
                     + self.accel.to_bytes(4, byteorder = 'little')
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def chLspeed(self, speed):
        self.speed = speed
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[2]                                   \
                     + self.mCom[2]                                      \
                     + self.speed.to_bytes(4, byteorder = 'little')
        if not self.writeSerial(self.payload):
            return False

        self.payload1 = os.urandom(1)                                    \
                      + self.address[0]                                  \
                      + self.address[2]                                  \
                      + self.mCom[3]                                     \
                      + self.speed.to_bytes(4, byteorder = 'little')
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def chRspeed(self, speed):
        self.speed = speed
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[3]                                   \
                     + self.mCom[2]                                      \
                     + self.speed.to_bytes(4, byteorder = 'little')
        if not self.writeSerial(self.payload):
            return False

        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[3]                                   \
                     + self.mCom[3]                                      \
                     + self.speed.to_bytes(4, byteorder = 'little')
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def chBspeed(self, speed):
        self.speed = speed
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[8]                                   \
                     + self.mCom[2]                                      \
                     + self.speed.to_bytes(4, byteorder = 'little')
        if not self.writeSerial(self.payload):
            return False

        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[8]                                   \
                     + self.mCom[3]                                      \
                     + self.speed.to_bytes(4, byteorder = 'little')
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def staLmoto(self):
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[2]                                   \
                     + self.mCom[6]                                      \
                     + os.urandom(4)
        if not self.writeSerial(self.payload):
            return False

        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[2]                                   \
                     + self.mCom[0]                                      \
                     + os.urandom(4)
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def staRmoto(self):
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[3]                                   \
                     + self.mCom[6]                                      \
                     + os.urandom(4)
        if not self.writeSerial(self.payload):
            return False

        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[3]                                   \
                     + self.mCom[0]                                      \
                     + os.urandom(4)
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def staBmoto(self):
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[8]                                   \
                     + self.mCom[6]                                      \
                     + os.urandom(4)
        if not self.writeSerial(self.payload):
            return False

        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[8]                                   \
                     + self.mCom[0]                                      \
                     + os.urandom(4)
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def staRLmoto(self):
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[2]                                   \
                     + self.mCom[5]                                      \
                     + os.urandom(4)
        if not self.writeSerial(self.payload):
            return False

        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[2]                                   \
                     + self.mCom[0]                                      \
                     + os.urandom(4)
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def staRRmoto(self):
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[3]                                   \
                     + self.mCom[5]                                      \
                     + os.urandom(4)
        if not self.writeSerial(self.payload):
            return False

        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[3]                                   \
                     + self.mCom[0]                                      \
                     + os.urandom(4)
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def staRBmoto(self):
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[8]                                   \
                     + self.mCom[5]                                      \
                     + os.urandom(4)
        if not self.writeSerial(self.payload):
            return False

        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[8]                                   \
                     + self.mCom[0]                                      \
                     + os.urandom(4)
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def stoLmoto(self):
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[2]                                   \
                     + self.mCom[1]                                      \
                     + os.urandom(4)
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def stoRmoto(self):
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[3]                                   \
                     + self.mCom[1]                                      \
                     + os.urandom(4)
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def stoBmoto(self):
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[8]                                   \
                     + self.mCom[1]                                      \
                     + os.urandom(4)
        if self.writeSerial(self.payload):
            return True
        else:
            return False

    def writeRelay(self, relays):
        self.relays = relays
        self.payload = os.urandom(1)                                     \
                     + self.address[0]                                   \
                     + self.address[17]                                  \
                     + self.sCom[0]                                      \
                     + self.relays.to_bytes(4, byteorder = 'little')
        if self.writeSerial(self.payload):
            return True
        else:
            return False

def main():
    print("Hello world!")

if __name__ == '__main__':
    main()
