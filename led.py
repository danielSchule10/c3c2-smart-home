import RPi.GPIO as GPIO

# LED / GPIO Hilfsfunktionen (minimalistisch)

def usable(pin):
    """Testet ob Pin HIGH wird (Blocking bis erster Read)"""
    try:
        # Set up the GPIO pin
        GPIO.setmode(GPIO.BCM)
        # Set the pin as an input with an optional pull-up or pull-down resistor
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
        while True:
            # Read the state of the pin
            if GPIO.input(pin):
                return True
            else:
                return False
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup(pin)

def setup_led(pin):
    """Richtet Pin als OUTPUT ein"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    return True

def clear_led(pin):
    """Gibt Pin wieder frei"""
    GPIO.cleanup(pin)

class get:
    # Leseoperationen
    def led(pin):
        try:
            if GPIO.input(pin) == GPIO.HIGH:
                return True
            else:
                return False
        except:
            return False
        
class set:
    # Schreiboperationen
    def led_on(pin, repeat=False):
        try:
            GPIO.output(pin, GPIO.HIGH)
            return True

        except RuntimeError as e:
            if repeat:
                return False
            else:
                setup_led(pin)
                set.led_on(pin, True)

    def led_off(pin, repeat=False):
        try:
            GPIO.output(pin, GPIO.LOW)
            return True

        except RuntimeError as e:
            if repeat:
                return False
            else:
                setup_led(pin)
                set.led_off(pin, True)
                print('x')

    def led(pin, state):
        """Schaltet LED anhand Bool/Keyword"""
        if isinstance(state, bool):
            if state:
                set.led_on(pin)
            else:
                set.led_off(pin)
        elif state.upper() in ["ON", "HIGH"]:
            set.led_on(pin)
        elif state.upper() in ["OFF", "LOW"]:
            set.led_off(pin)
        else:
            raise False
        
    def switch(pin):
        """Toggle Zustand"""
        if get.led(pin):
            set.led_off(pin)
            return False
        else:
            set.led_on(pin)
            return True

class Cleanup:
    def __del__(self):
        # Fallback Clean-up beim GC
        GPIO.cleanup()

cleanup_instance = Cleanup()