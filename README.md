HOME ASSISTANT AUTOMATION PROJECT – SUMMARY REPORT
Name: Subash Shankar
Register Number: 42111293
Course: Internet of Things
Project Title: MQTT Sensor Integration with Home Assistant
Date: 07/12/2025
1. Objective
The objective of this project is to implement an IoT automation system using MQTT, Python, and Home
Assistant.
Sensors used: Temperature, Humidity, and Light Level.
The system demonstrates real-time data publishing, subscribing, and dashboard visualization.
2. System Architecture
1. Python script publishes JSON sensor data to the MQTT topic:
home/subash-2025/sensor
2. Mosquitto MQTT Broker (Docker) receives the published data.
3. MQTT Subscriber validates real-time data.
4. Home Assistant subscribes to the MQTT topic and displays values on the dashboard.
3. Technologies Used- Python, Paho-MQTT Library- MQTT Protocol- Docker (Mosquitto + Home Assistant)- YAML configuration- Home Assistant Dashboard
4. Steps Performed
4.1 MQTT Broker Setup- Installed Docker- Started Mosquitto broker container- Verified using: docker ps
4.2 Python MQTT Publisher
Published Temperature, Humidity & Light Level values every 5 seconds.
4.3 MQTT Subscriber
Command used:
docker exec -it mqtt mosquitto_sub -h host.docker.internal -p 1883 -t "home/subash-2025/sensor"
4.4 Home Assistant Setup- Installed Home Assistant (Docker)- Added MQTT integration- Configured sensors in configuration.yaml:
mqtt:
sensor:- name: "Temperature"
state_topic: "home/subash-2025/sensor"
value_template: "{{ value_json.temperature }}"
unit_of_measurement: "°C"- name: "Humidity"
state_topic: "home/subash-2025/sensor"
value_template: "{{ value_json.humidity }}"
unit_of_measurement: "%"- name: "Light Level"
state_topic: "home/subash-2025/sensor"
value_template: "{{ value_json.light }}"
unit_of_measurement: "lx"
4.5 Dashboard Creation
Added Entities card showing all three sensor values.
5. Results Obtained- MQTT broker successfully received real-time data.- Subscriber displayed JSON sensor values.- Home Assistant dashboard visualized Temperature, Humidity, and Light Level live.- Completed custom sensor requirement (Light Level).
6. Conclusion
This project demonstrates end-to-end IoT communication using MQTT and Home Assistant, showing
sensor integration, automation, and dashboard visualization# home-assistant-mqtt-assignment
