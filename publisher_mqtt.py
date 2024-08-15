import paho.mqtt.client as mqtt
import time
import random

# MQTT Broker configuration
broker = "test.mosquitto.org"
port = 1883
temperature_topic = "iot/sensor/temperature"
humidity_topic = "iot/sensor/humidity"

# Create MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect(broker, port)

def publish_data():
    while True:
        temperature = random.uniform(20.0, 25.0)
        humidity = random.uniform(30.0, 60.0)
        client.publish(temperature_topic, temperature)
        client.publish(humidity_topic, humidity)
        print(f"Published: Temperature = {temperature} to topic: {temperature_topic}")
        print(f"Published: Humidity = {humidity} to topic: {humidity_topic}")
        time.sleep(5)  # Send data every 5 seconds

publish_data()