import RPi.GPIO as GPIO

# Generische Button-Basis (Ereignis -> trigger())

class GenericButtonHandler:
    """Basis-Klasse für Button-Logik (GPIO Event)"""
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

    # Pin Setup (Input mit Pull-Down + Output LOW)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup(input_pin)
        GPIO.setup(self.input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.output_pin, GPIO.OUT, initial=GPIO.LOW)

    # Standard Event Registrierung
        self.setup_event_detection()

        print("Button instantiated")

    def setup_event_detection(self):
        """Richtet Event-Erkennung ein (überschreibbar)"""
        GPIO.add_event_detect(
            self.input_pin,
            self.event,
            callback=self.trigger,
            bouncetime=self.bouncetime
        )

    def trigger(self, pin):
        """Wird von konkreter Button-Klasse implementiert"""
        pass
