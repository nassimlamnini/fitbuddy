while True:
    data = {
        "sensor_id": 1,
        "left_side_force": 50.0,
        "right_side_force": 45.0,
        "imbalance_percentage": 10.0
    }
    client.publish("asymmetry/data", json.dumps(data))
    print("Asymmetry Data Sent:", data)
    time.sleep(5)
