import RPi.GPIO as GPIO
import time

PIR_PIN = 4
LED_PIN = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Initializing PIR Sensor...")
time.sleep(2)  # Sensor stabilization
print("System Ready!")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            print("No Motion")
            GPIO.output(LED_PIN, GPIO.LOW)
        
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program Stopped")
    GPIO.cleanup()
