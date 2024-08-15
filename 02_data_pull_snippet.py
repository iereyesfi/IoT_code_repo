import requests
import time

# Reemplaza con tu propia API key de lectura de ThinkSpeak y el número de canal
API_KEY = 'TU_API_KEY'
CHANNEL_ID = 'TU_CHANNEL_ID'

# Función para obtener datos de temperatura en tiempo real desde ThinkSpeak
def get_temperature_data():
    url = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/1.json?api_key={API_KEY}&results=1'
    response = requests.get(url)
    data = response.json()
    feeds = data['feeds']
    if feeds:
        latest_entry = feeds[-1]
        temperature = float(latest_entry['field1'])
        return {'sensor_id': CHANNEL_ID, 'temperature': temperature, 'timestamp': latest_entry['created_at']}
    return None
