import paho.mqtt.client as mqtt
import time
import json

# Mandatory details
student_name = "Subash Shankar"
unique_id = "YOUR_REGISTER_NUMBER"

# Unique topic
topic = "home/subash-2025/sensor"

# MQTT broker details
broker = "localhost"
port = 1883

client = mqtt.Client()
client.connect(broker, port)

while True:
    data = {
        "temperature": 25,
        "humidity": 60,
        "light": 300
    }

    client.publish(topic, json.dumps(data))
    print("Published:", data)
    time.sleep(5)
