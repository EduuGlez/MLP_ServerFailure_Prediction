import numpy as np
import pandas as pd

np.random.seed(42)

# Número de muestras
num_samples = 5000
data = []

for i in range(num_samples):
    # Valores de los registros
    temperature = np.random.normal(60, 12) # temperatura
    cpu_usage = np.random.normal(55, 22) # porcentaje de uso de CPU
    memory_usage = np.random.normal(65, 18) # porcentaje de uso de memoria
    network_traffic = np.random.normal(350, 150) # trafico de red en Mbps

    # Limitar rangos para evitar valores extremos poco realistas
    temperature = np.clip(temperature, 20, 100)
    cpu_usage = np.clip(cpu_usage, 0, 100)
    memory_usage = np.clip(memory_usage, 0, 100)
    network_traffic = np.clip(network_traffic, 10, 1000)

    # Variable objetivo: fallo (0 o 1)
    failure = 0

    # Temperatura crítica + CPU alta
    if temperature > 75 and cpu_usage > 80:
        failure = 1

    # Memoria saturada + CPU alta
    elif memory_usage > 85 and cpu_usage > 75:
        failure = 1

    # Tráfico extremo + CPU alta
    elif network_traffic > 700 and cpu_usage > 70:
        failure = 1

    # Condición combinada 
    elif (
        temperature > 65 and 
        cpu_usage > 65 and 
        memory_usage > 70 and 
        np.random.rand() > 0.5
    ):
        failure = 1

    # Condición aleatoria para introducir ruido
    elif np.random.rand() < 0.05:
        failure = 1

    # Agregar el registro a la lista de datos
    data.append([
        temperature,
        cpu_usage,
        memory_usage,
        network_traffic,
        failure
    ])

# Crear DataFrame
df = pd.DataFrame(data, columns=[
    "temperature",
    "cpu_usage",
    "memory_usage",
    "network_traffic",
    "failure"
])

# Guardar CSV
df.to_csv("sensor_data.csv", index=False)
print(df["failure"].value_counts())