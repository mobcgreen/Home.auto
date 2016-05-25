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
pir = Pir(rpi, 14)

light = False
while True:
    if pir.pir_motion():
        if not light:
            buzzer.buz_on()
            sleep(2)
            light = True
            pir.pir_motion = False
        elif light:
            buzzer.buz_off()
            light = False
            pir.pir_motion = False
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

motion = True
while False:
    if pir.pir_motion():
        if not motion:
            buzzer.buz_off()
            motion = True
            pir.pir_motion = True
        elif motion:
            buzzer.buz_on()
            motion = False
            pir.pir_motion = True
'''
    #sequence = [rgb.blue_on(), rgb.green_on(), rgb.red_on()]

    #for light in sequence:
    #    sequence(light)
    #    sleep(1)
