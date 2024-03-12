import json
from pulsar import Client, Message

# Configura la URL del servidor Pulsar
pulsar_url = "pulsar://localhost:6650"

# Configura el nombre del tema al que deseas enviar mensajes
topic_name = "persistent://public/default/crear-compania9"
producer = None
try:
    # Crea un cliente Pulsar
    client = Client(pulsar_url)

    # Crea un productor para el tema
    producer = client.create_producer(topic_name)

    # Envía un mensaje al tema
    data = {"name": "Alice", "age": 30, "address": {"street": "Main St", "city": "New York"}}
    example_data = {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "123 Main Street",
                "city": "Anytown"
            }
        }
        # Serialize the data as JSON string
    serialized_data = json.dumps(example_data).encode('utf-8')
    mensaje = "Hola, esto es un mensaje de ejemplo"
    producer.send(serialized_data)

    # Espera la pulsación de una tecla para finalizar

except Exception as e:
    print("Error:", str(e))

finally:
    # Cierra el productor y el cliente
    producer.close()
    client.close()
