from time import sleep

class Button:
    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.__pin = pin
        self.__setup_button()
        self.__pressed = False

    @property
    def pressed(self):
        return self.__pressed

    @pressed.setter
    def pressed(self, value):
        self.__pressed = value


    def __setup_button(self, resistor=True):
        if not resistor:
            self.__board.GPIO.setup(self.__pin, self.__board.GPIO.IN)
            print('Button set up on pin: ' + str(self.__pin))
        elif resistor:
            self.__board.GPIO.setup(self.__pin, self.__board.GPIO.IN, pull_up_down=self.__board.GPIO.PUD_UP)
        else:
            print('Error setting up resistor')

        # add interrupt
        self.__board.GPIO.add_event_detect(self.__pin, self.__board.GPIO.FALLING, callback=self.__my_callback, bouncetime=300)
        print('DEBUG: Set up interrupt')
    def __my_callback(self, channel):
        print('DEBUG: Callback ran')
        self.pressed = True



if __name__ == "__main__":
    from board import Board
    rpi = Board()
    print('DEBUG: Board instance created')
    button = Button(rpi, 22)
    print('DEBUG: Button set up on pin 22')
    while True:
        if button.pressed:
            print('button pressed')
            button.pressed = False
    rpi.GPIO.cleanup()
