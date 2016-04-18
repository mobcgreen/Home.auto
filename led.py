class Led:
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.__pin = pin
        self.__setup_led()

    def __setup_led(self):
        self.__board.GPIO.setup(self.__pin, self.__board.GPIO.OUT)

    def led_on(self):
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.HIGH)

    def led_off(self):
        self.__board.GPIO.output(self.__pin, self.__board.GPIO.LOW)

if __name__ == "__main__":
    from board import Board
    from time import sleep
    rpi = Board()
    led = Led(rpi, 13)
    led.led_on()
    sleep(3)
    led.led_off()

