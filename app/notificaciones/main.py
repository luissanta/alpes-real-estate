import os
import pulsar


<<<<<<< HEAD
class EventoDominio(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
=======
>>>>>>> develop

# Configura la URL del servidor Pulsar
pulsar_url = "pulsar://localhost:6650"

<<<<<<< HEAD
class EventoDominioReservaCreada(EventoDominio):
    data = ReservaCreadaPayload()

HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe('eventos-reserva', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='sub-notificacion-eventos-reservas', schema=AvroSchema(EventoDominioReservaCreada))
=======
# Configura el nombre del tema al que deseas suscribirte
topic_name = "persistent://public/default/eventos-reserva"

# Configura el nombre de la suscripción
subscription_name = "aeroalpes-sub-eventos"

client = pulsar.Client('pulsar://localhost:6650')
#crear-compania8
consumer = client.subscribe('response-company', 'my-subscription')

HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")



#schema_dict = {"type": "record", "name": "Example", "fields": [{"name": "field1", "type": "string"}, {"name": "field2", "type": "int"}]}

>>>>>>> develop

while True:


    try:
        while True:
            msg = consumer.receive()
            try:
              
                print("Mensaje recibido: {}".format(msg.data().decode('utf-8')))
             

            except Exception as e:
            
                print("Error al procesar el mensaje:", str(e))

            finally:
                consumer.acknowledge(msg)

    except KeyboardInterrupt:
        pass

    finally:
        consumer.close()
        client.close()