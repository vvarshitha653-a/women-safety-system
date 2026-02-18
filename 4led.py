import RPi.GPIO as GPIO
import time

# Use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

# LED Pins
led_pins = [17, 18, 27, 22]

# Button Pins
button_pins = [5, 6, 13, 19]

# Setup LED pins as OUTPUT
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Setup Button pins as INPUT with pull-up resistor
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        for i in range(4):
            if GPIO.input(button_pins[i]) == GPIO.LOW:
                GPIO.output(led_pins[i], GPIO.HIGH)
            else:
                GPIO.output(led_pins[i], GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
