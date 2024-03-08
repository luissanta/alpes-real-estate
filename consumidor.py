from pulsar import ConsumerType, Client, Message

# Configura la URL del servidor Pulsar
pulsar_url = "pulsar://localhost:6650"

# Configura el nombre del tema al que deseas suscribirte
topic_name = "persistent://public/default/crear-compania9"

# Configura el nombre de la suscripción
subscription_name = "aeroalpes-sub-eventos"

# Crea un cliente Pulsar
client = Client(pulsar_url)

# Crea un consumidor
consumer = client.subscribe(
    topic_name,
    subscription_name,
    consumer_type=ConsumerType.Shared  # Puedes ajustar el tipo de consumidor según tus necesidades
)

try:
    # Bucle para recibir mensajes
    while True:
        msg = consumer.receive()
        try:
            # Procesa el mensaje
            print("Mensaje recibido: {}".format(msg.data().decode('utf-8')))
            # Realiza acciones adicionales según tus necesidades

        except Exception as e:
            # Maneja cualquier excepción al procesar el mensaje
            print("Error al procesar el mensaje:", str(e))

        finally:
            # Marca el mensaje como consumido
            consumer.acknowledge(msg)


finally:
    # Cierra el consumidor y el cliente al finalizar
    consumer.close()
    client.close()
