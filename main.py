from board import Board
from led import Led
from rgb import RGB_led
from button import Button
from buzzer import Buzzer
from pir import Pir
from temp import Temperature
from time import sleep
rpi = Board()

led = Led(rpi, 13)
led = RGB_led(rpi, 20, 21, 16)
button = Button(rpi, 22)
buzzer = Buzzer(rpi, 24)
pir = Pir(rpi, 14)

if button.pressed:
    led.green_on()

