import time
import random
import threading
import pandas as pd

# Simulación de dispositivos IoT que generan datos
def edge_device(device_id):
    data = {
        'timestamp': [],
        'device_id': [],
        'temperature': [],
        'humidity': []
    }
    for _ in range(10):  # Simulación de 10 lecturas de sensor
        timestamp = time.time()
        temperature = random.uniform(20.0, 30.0)
        humidity = random.uniform(30.0, 70.0)
        data['timestamp'].append(timestamp)
        data['device_id'].append(device_id)
        data['temperature'].append(temperature)
        data['humidity'].append(humidity)
        time.sleep(1)  # Espera de 1 segundo entre lecturas
    return pd.DataFrame(data)

# Simulación de Fog Computing: Agregación de datos de múltiples dispositivos
def fog_node(device_data_list):
    aggregated_data = pd.concat(device_data_list)
    aggregated_data['avg_temperature'] = aggregated_data['temperature'].mean()
    aggregated_data['avg_humidity'] = aggregated_data['humidity'].mean()
    return aggregated_data

# Simulación de Roof Computing: Coordinación y optimización de recursos
def roof_node(fog_data_list):
    roof_data = pd.concat(fog_data_list)
    roof_data['overall_avg_temperature'] = roof_data['avg_temperature'].mean()
    roof_data['overall_avg_humidity'] = roof_data['avg_humidity'].mean()
    return roof_data

# Simulación de Cloud Computing: Almacenamiento y procesamiento avanzado
def cloud_processing(roof_data):
    # Aquí podrías agregar procesamiento avanzado, almacenamiento en la nube, etc.
    print("Datos procesados en la nube:")
    print(roof_data)

# Función principal para la simulación
def main_simulation():
    # Simulación de Edge Computing
    edge_data_list = []
    for i in range(5):  # Simulación de 5 dispositivos IoT
        edge_data_list.append(edge_device(f'device_{i+1}'))
    
    # Simulación de Fog Computing
    fog_data = fog_node(edge_data_list)
    
    # Simulación de Roof Computing
    roof_data = roof_node([fog_data])
    
    # Simulación de Cloud Computing
    cloud_processing(roof_data)

if __name__ == "__main__":
    main_simulation()
