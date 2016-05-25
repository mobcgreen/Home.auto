from time import sleep

class Pir:

    def __init__(self, gpio_object, pin):
        self.__board = gpio_object
        self.__pirpin = pin
        self.__setup_pir()

    def __setup_pir(self):
        self.__board.GPIO.setup(self.__pirpin, self.__board.GPIO.IN)

    def pir_motion(self):
        print ('PIR Module Test(CTRL + C to exit)')
        sleep(2)
        print ('Ready')
        while True:
            #print('im running')
            if self.__board.GPIO.input(self.__pirpin):
                #print(self.__board.GPIO.input(self.__pirpin))
                print ('Motion Detected!')
            else:
                #print(self.__board.GPIO.input(self.__pirpin))
                print ('Not Detected :(')
            sleep(1)


if __name__ == '__main__':
    from board import Board
    #from time import sleep
    rpi = Board()
    pir = Pir(rpi, 6)
    pir.pir_motion()
    rpi.GPIO.cleanup()







