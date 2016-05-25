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
rgb = RGB_led(rpi, 20, 21, 16)
button = Button(rpi, 22)
buzzer = Buzzer(rpi, 24)
buzzer2 = Buzzer(rpi, 7)
pir = Pir(rpi, 14)
'''
light = False
while True:
    if button.pressed:
        if not light:
            led.led_on()
            light = True
            button.pressed = False
        elif light:
            led.led_off()
            light = False
            button.pressed = False
'''
buz = False
while True:
    if button.pressed:
        if not buz:
            buzzer2.buz_on()
            buz = True
            button.pressed = False
        elif buz:
            buzzer2.buz_off()
            buz = False
            button.pressed = False

    #sequence = [rgb.blue_on(), rgb.green_on(), rgb.red_on()]

    #for light in sequence:
    #    sequence(light)
    #    sleep(1)
