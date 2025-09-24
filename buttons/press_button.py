import RPi.GPIO as GPIO
from .button import GenericButtonHandler 

# Momentan-Taster: aktiviert Output bei Event

class PressButton(GenericButtonHandler):
    def __init__(self, input_pin, output_pin, bouncetime=200):
        # We want to catch both RISING and FALLING so we can 
        # handle the pin going high (button press) and low (button release).
        super().__init__(
            input_pin=input_pin,
            output_pin=output_pin,
            event=GPIO.BOTH,
            bouncetime=bouncetime
        )

    def trigger(self, pin):
        # Einfach: immer HIGH setzen (kurzer Impuls)
        print(f"triggered push button on {self.input_pin}")
        GPIO.output(self.output_pin, GPIO.HIGH)
