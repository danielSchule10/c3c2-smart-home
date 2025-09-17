import RPi.GPIO as GPIO

class GenericButtonHandler:
    """
    A base class for handling button presses on a Raspberry Pi. 
    Subclasses can override or extend functionality
    """
    def __init__(
        self, 
        input_pin, 
        output_pin, 
        event=GPIO.RISING, 
        bouncetime=200
    ):
        self.input_pin = input_pin
        self.output_pin = output_pin
        self.event = event
        self.bouncetime = bouncetime

        # Pin setup
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup(input_pin)
        GPIO.setup(self.input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.output_pin, GPIO.OUT, initial=GPIO.LOW)

        # Setup default event detection
        self.setup_event_detection()

        print("Button instantiated")

    def setup_event_detection(self):
        """
        Set up the GPIO event detection. 
        Subclasses can override this if they need different behavior
        (e.g., GPIO.BOTH instead of GPIO.RISING).
        """
        GPIO.add_event_detect(
            self.input_pin,
            self.event,
            callback=self.trigger,
            bouncetime=self.bouncetime
        )

    def trigger(self, pin):
        """
        The action that the button should perform upon triggering.
        Overwrite this in subclasses to implement custom functionality.
        """
        pass
