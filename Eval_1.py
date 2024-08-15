import random
import time
import requests

# Function to simulate sensor data
def simulate_sensor_data():
    temperature = round(random.uniform(20.0, 30.0), 2) # Simulatetemperature between 20.0 and 30.0 degrees Celsius
    humidity = round(random.uniform(30.0, 70.0), 2) # Simulate humidity between 30.0% and 70.0%
    return temperature, humidity

# ThingSpeak API parameters
THINGSPEAK_API_KEY = '221QYYI2HEYQ67YL'
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

while True:
    # Get simulated sensor data
    temperature, humidity = simulate_sensor_data()

    # Print simulated data
    print(f'Simulated Temp={temperature}*C Humidity={humidity}%')

    # Send data to ThingSpeak
    payload = {'api_key': THINGSPEAK_API_KEY, 'field1': temperature, 'field2': humidity}
    response = requests.post(THINGSPEAK_URL, data=payload)

    if response.status_code == 200:
        print('Data sent to ThingSpeak successfully!')
    else:
        print('Failed to send data to ThingSpeak.')
    # Wait 10 seconds before next read
    time.sleep(30)