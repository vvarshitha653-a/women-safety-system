import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24
LED = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(TRIG, False)
print("Waiting for sensor to settle...")
time.sleep(2)

try:
    while True:
        # Send trigger pulse
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Measure pulse duration
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while G
