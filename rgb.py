
class RGB_led:
    def __int__(self, gpio_object, r, g, b):
        self.__red_pin = r
        self.__green_pin = g
        self.__blue_pin = b
        self.__outputs = [self.__red_pin, self.__blue_pin, self.__green_pin]
        self.__board = gpio_object

        self.__setup_pins()

    def __setup_pins(self):
        print('DEBUGGING: Setting up outputs')

        for pin in self.__outputs:
            self.__board.GPIO.setup(pin, self.__board.GPIO.OUT)

    def red_on(self):
        '''red led turns on'''
        self.turn_off()
        self.__board.GPIO.output(self.__red_pin, self.__board.GPIO.HIGH)

    def green_on(self):
        '''green led turns on'''
        self.turn_off()
        self.__board.GPIO.output(self.__green_pin, self.__board.GPIO.HIGH)

    def blue_on(self):
        '''blue led turns on'''
        self.turn_off()
        self.__board.GPIO.output(self.__blue_pin, self.__board.GPIO.HIGH)

    def turn_off(self):
        '''turns all the leds off before'''
        for pin in self.__outputs:
            self.__board.GPIO.output(pin, self.__board.GPIO.LOW)

if __name__ == "__main__":
    from board import Board
    from time import sleep
    B = Board
    led = RGB_led(B, 21, 20, 16)

    led.red_on()
    sleep(3)
    led.turn_off()
    led.green_on()
    sleep(3)
    led.turn_off()
    led.blue_on()
    sleep(3)
    led.turn_off()











