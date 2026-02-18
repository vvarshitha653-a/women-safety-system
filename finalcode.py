from gpiozero import LED, Button
import requests
import time

# GPIO
TOUCH_PIN = 17
LED_PIN = 27

touch = Button(TOUCH_PIN, pull_up=False)
led = LED(LED_PIN)

# Telegram
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def get_location():
    try:
        res = requests.get("http://ip-api.com/json/", timeout=5)
        data = res.json()
        location = f"{data['city']}, {data['regionName']}, {data['country']}"
        return location
    except:
        return "Location unavailable"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

def emergency():
    print("🚨 Emergency Triggered")

    for _ in range(3):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

    location = get_location()

    msg = (
        "🚨 WOMEN SAFETY ALERT 🚨\n\n"
        "Touch sensor activated!\n"
        f"📍 Location: {location}\n"
        "Immediate help required!"
    )

    send_telegram(msg)
    print("Telegram alert sent")

touch.when_pressed = emergency

print("System Ready – Touch sensor active")

while True:
    time.sleep(1)
