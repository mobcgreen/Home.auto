import RPi.GPIO as GPIO
from time import sleep

class Board:

    def __int__(self):
        '''Enables GPIO on Raspberry Pi.

        :param GPIO: RPi.GPIO on the Raspberry Pi
        :param rpi_version: Version of the GPIO libary
        :param mode: Current board mode

        :returns none:
        '''

        self.GPIO = RPi.GPIO
        self.setupGPIO()
        self.rpi_version = self.GPIO.VERSION
        self.mode = self.GPIO.getmode()

    def setupGPIO(self):
        '''Puts the Raspberry Pi into the correct mode (BCM) and disbles warnings.'''

        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)

    def clean_up(self):
        '''Cleans up assigned GPIO pins on the Raspberry Pi'''

        self.GPIO.clean()

    

