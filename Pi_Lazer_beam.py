//pip install toneac
import time
import serial
from toneac import ToneAC

BUZZER_PIN = 8
ser = serial.Serial(8, 7, baudrate=115200)
TFmini = None


def setup():
    global TFmini
    TFmini = DFRobot_TFmini()
    TFmini.begin(ser)


def loop():
    global TFmini
    if TFmini.measure():
        dis = TFmini.getDistance()
        power = TFmini.getPower()
        print(f"Distance = {dis} mm")

        if dis <= 100:
            play_tone(1000000, 10)
        else:
            no_tone_ac()


def play_tone(frequency, duration):
    ToneAC(BUZZER_PIN, frequency, duration * 1000)


def no_tone_ac():
    ToneAC.off(BUZZER_PIN)


class DFRobot_TFmini:
    def begin(self, serial_obj):
        self.serial = serial_obj

    def measure(self):
        self.serial.write(b'\x42\x57')
        time.sleep(0.1)
        if self.serial.in_waiting >= 7:
            data = self.serial.read(7)
            if data[0] == 0x59 and data[1] == 0x59:
                dis = data[2] + data[3] * 256
                power = data[4] + data[5] * 256
                return True
        return False

    def getDistance(self):
        return dis

    def getPower(self):
        return power


if __name__ == "__main__":
    setup()
    while True:
        loop()
