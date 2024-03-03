from pulsar import Client, Message

# Configura la URL del servidor Pulsar
pulsar_url = "pulsar://localhost:6650"

# Configura el nombre del tema al que deseas enviar mensajes
topic_name = "persistent://public/default/tu-topico"

try:
    # Crea un cliente Pulsar
    client = Client(pulsar_url)

    # Crea un productor para el tema
    producer = client.create_producer(topic_name)

    # Envía un mensaje al tema
    mensaje = "Hola, esto es un mensaje de ejemplo"
    producer.send(mensaje.encode('utf-8'))

    # Espera la pulsación de una tecla para finalizar
    input("Presiona una tecla para finalizar...")

except Exception as e:
    print("Error:", str(e))

finally:
    # Cierra el productor y el cliente
    producer.close()
    client.close()
