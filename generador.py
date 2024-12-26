import random
import json
from datetime import datetime, timedelta

# Empresas y fuentes disponibles
companies = ["BMA", "YPF", "GGAL", "PAMP", "TS"]
sources = ["A", "B"]

# Función para generar un timestamp aleatorio
def generate_random_timestamp():
    # Rango de fechas (desde hoy hasta 30 días atrás)
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    # Convertir a milisegundos
    return int(random_date.timestamp() * 1000)

# Generar registros
records = []
for _ in range(100):
    record = {
        "name": random.choice(companies),
        "buy": round(random.uniform(70.0, 250.0), 2),  # Valores entre 70.0 y 250.0
        "sell": round(random.uniform(70.0, 250.0), 2),
        "timestamp": generate_random_timestamp(),
        "source": random.choice(sources),
    }
    # Asegurar que "sell" sea mayor que "buy"
    if record["sell"] < record["buy"]:
        record["sell"], record["buy"] = record["buy"], record["sell"]
    records.append(record)

# Mezclar los registros
random.shuffle(records)

# Guardar en un archivo JSON
output_file = "generated_records.json"
with open(output_file, "w") as file:
    json.dump(records, file, indent=4)

print(f"100 registros generados y guardados en {output_file}")
