class Led:
    def __init__(self, gpio_object, pin):
        self._board = gpio_object
        self._pin = pin
        self._setup_led()

    def _setup_led(self):
        self._board.GPIO.setup(self._pin, self._board.GPIO.OUT)

    def led_on(self):
        self._board.GPIO.output(self._pin, self._board.GPIO.HIGH)

    def lef_off(self):
        self._board.GPIO.output(self._pin, self._board.GPIO.LOW)


