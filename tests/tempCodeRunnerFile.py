import paho.mqtt.client as mqtt
import json
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    data = {
        "repetitions": 12,
        "duration": 25.5,
        "difficulty": 0.7,
        "speed": 3.2,
        "amplitude": 1.5
    }
    client.publish("sensor/data", json.dumps(data))
    print("Sensor Data Sent:", data)
    time.sleep(5)
