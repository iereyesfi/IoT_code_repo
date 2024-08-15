import random
import time
import json
import time
import requests
from   colorama import Fore

THINGSPEAK_WRITE_API_KEY     = '221QYYI2HEYQ67YL'
THINGSPEAK_READ_API_KEY      = 'D0ZKTH7JPRQO5FZ3'
THINGSPEAK_CHANNEL_ID        = '2576157'
THINGSPEAK_TEMPERATURE_FIELD = '1'
TRANSMISSION_THINKSPEAK_URL  = 'https://api.thingspeak.com/update'
SUCCESSFULLY_TRANSMISSION    = 200
Request_response             = False

# Step 1: Data transmission from simulated sensor to Thinkspeak cloud service
def simulate_sensor_data():
    Temperature = round(random.uniform(-10, 40), 2) # Simulatetemperature between -10 and 40 degrees Celsius
    return Temperature

# Step 2: # Send data to ThingSpeak
def transmit_data(Temperature):
    Transmission_payload = {'api_key': THINGSPEAK_WRITE_API_KEY, 'field1': Temperature}
    response = requests.post(TRANSMISSION_THINKSPEAK_URL, data = Transmission_payload)
    global Request_response
    if response.status_code == SUCCESSFULLY_TRANSMISSION:
        Request_response = True
    else:
        Request_response = False 
    return json.dumps(Temperature)

# Step 3: Get temperature sensor data from Thinkspeak cloud service
def get_temperature_data(read_API_key , channel_ID, channel_FIELD):    
    Temperature_url = 'https://api.thingspeak.com/channels/' + channel_ID + '/feeds.json?api_key=' + read_API_key + '&results=1'
    Temperature_response = requests.get(Temperature_url)
    Temperature_data = Temperature_response.json()
    Temperature_feeds = Temperature_data['feeds']
    if Temperature_feeds:
        Temperature_last_entry = Temperature_feeds[-1]
        Temperature = float(Temperature_last_entry['field1'])
        return json.dumps({'sensor_id': channel_ID, 'temperature': Temperature, 'timestamp': Temperature_last_entry['created_at']})
    return None

# Paso 4: Procesar los datos recibidos y detectar anomalías
def process_data(data_json):
    data = json.loads(data_json)
    anomalies = []
    if data['temperature'] < 0 or data['temperature'] > 35: anomalies.append(data)
    return anomalies

# Paso 5: Tomar acciones basadas en las anomalías detectadas
def take_action(anomalies):
    for anomaly in anomalies:
        print(f"{Fore.RED} Alerta: Temperatura anómala detectada en el sensor {anomaly['sensor_id']} con {anomaly['temperature']} °C")

# Ejecutar la práctica completa
while True:
    # Get simulated sensor data
    Temperature = simulate_sensor_data()

    # Transmit Simulated Sensor data to Thinkspeak cloud service
    transmitted_data = transmit_data(Temperature)

    if Request_response:
        # Print transmitted Simulated Sensor data to Thinkspeak cloud service
        print(f"{Fore.WHITE} Datos transmitidos:", transmitted_data)
    
        # Get last data from Thinkspeak cloud service
        sensor_data = get_temperature_data(THINGSPEAK_READ_API_KEY,THINGSPEAK_CHANNEL_ID, THINGSPEAK_TEMPERATURE_FIELD)
        print(f"{Fore.WHITE} Datos de sensores:", sensor_data)
    
        ## Process data and print anomalies
        anomalies = process_data(sensor_data)
        print(f"{Fore.WHITE} Anomalías detectadas:", anomalies)
        take_action(anomalies)

        # Wait 5 seconds until next simulated sensor data transmission to Thinkspeak cloud service
        time.sleep(30) 
    else:
        # Transmission error, do nothing
        print('Failed to send data to ThingSpeak.')
        # Wait 5 seconds until next simulated sensor data transmission to Thinkspeak cloud service
        time.sleep(30) 
