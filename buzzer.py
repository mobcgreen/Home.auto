import RPi.GPIO as gpio
import time

class Buzzer:

    def __init__(self, board, buzzerPin):
        self.board = board
        self.buzzerPin = buzzerPin
        self.buzzMethod()

    def buzzMethod(self):
        self.board.setup(buzzerPin, self.board.OUT)
        self.board.output(buzzerPin, HIGH)
        time.sleep(2)
        self.board.output(buzzerPin, LOW)

if __name__ == "__main__":
    from board import Board
    buzzerPin = 24
    board = Board()
    Buzzer(buzzerPin, board)