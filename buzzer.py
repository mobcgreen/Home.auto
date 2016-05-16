import RPi.GPIO as gpio
import time

class Buzzer:

    def __init__(self, gpio_object, buzzerPin):
        self._board = gpio_object
        self.buzzerPin = buzzerPin
        self.buzzMethod()
        print('setting up')

    def buzzMethod(self):
        self._board.setup(buzzerPin, self._board.OUT)
        print('setting output')
        self._board.output(buzzerPin, self._board.GPIO.HIGH)
        print('HIGH')
        time.sleep(2)
        self._board.output(buzzerPin, self._board.GPIO.LOW)
        print('LOW')

if __name__ == "__main__":
    from board import Board
    buzzerPin = 24
    board = Board()
    Buzzer(buzzerPin, board)