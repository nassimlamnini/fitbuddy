while True:
    data = {
        "sensor_id": 1,
        "battery_level": 85.0,
        "firmware_version": "1.0.3",
        "is_functional": True
    }
    client.publish("status/data", json.dumps(data))
    print("Sensor Status Sent:", data)
    time.sleep(5)
