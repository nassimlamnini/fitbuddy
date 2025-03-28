import paho.mqtt.client as mqtt
import json
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    data = {
        "accelerometer": "9.8",
        "gyroscope": "1.2",
        "magnetometer": "0.5"
    }
    client.publish("raw/data", json.dumps(data))
    print("Raw Data Sent:", data)
    time.sleep(5)
