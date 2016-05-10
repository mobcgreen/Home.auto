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

    def __setup_button(self):
            self.__board.GPIO.set(self.__pin, self.__board.GPIO.IN, pull_up_down=self.__board.GPIO.PUD_UP)
            #add interrupt
            self.__board.GPIO.add_event_detect(self.__pin, self.__board.GPIO.FALLING, callback=self.__my_callback, bouncetime=300)

    def __my_callback(self, channel):
        self.pressed = True

    if __name__ == "__main__":
        from board import Board
        from button import Button
        rpi = Board()
        button = Button(rpi, 22)

        while True:
            if button.pressed:
                print('button pressed')
                button.pressed = False
        rpi.GPIO.cleanup()


            
