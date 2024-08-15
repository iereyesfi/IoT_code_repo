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

def on_connect(client, userdata, flags, rc):
    if 0 == rc:
        print("Connected with result code " + str(rc) + " Connection successful")
    elif 1 == rc:
        print("Connected with result code " + str(rc) + " Connection refused - incorrect protocol version")
    elif 2 == rc:
        print("Connected with result code " + str(rc) + " Connection refused - invalid client identifier")
    elif 3 == rc:
        print("Connected with result code " + str(rc) + " Connection refused - server unavailable")
    elif 4 == rc:
        print("Connected with result code " + str(rc) + " Connection refused - bad username or password")
    elif 5 == rc:
        print("Connected with result code " + str(rc) + " Connection refused - not authorised")
    client.subscribe(temperature_topic)
    client.subscribe(humidity_topic)

def on_message(client, userdata, msg):
    if msg.topic == temperature_topic:
        print(f"Received: Temperature = {msg.payload.decode()} from topic: {msg.topic}")
    elif msg.topic == humidity_topic:
        print(f"Received: Humidity = {msg.payload.decode()} from topic: {msg.topic}")
        
# Configure callbacks
client.on_connect = on_connect
client.on_message = on_message
# Connect to the broker
client.connect(broker, port, 60)


def publish_data():
    temperature = random.uniform(20.0, 25.0)
    humidity = random.uniform(30.0, 60.0)
    client.publish(temperature_topic, temperature)
    client.publish(humidity_topic, humidity)
    print(f"Published: Temperature = {temperature} to topic: {temperature_topic}")
    print(f"Published: Humidity = {humidity} to topic: {humidity_topic}")
    
    #time.sleep(5) # Send data every 5 seconds
        
publish_data()
# Maintain connection and wait for messages
client.loop_forever()