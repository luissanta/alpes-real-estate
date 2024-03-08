import json
import pulsar

from app.moduls.lists.infrastructure.schema.v1.events import EventoDominioReservaCreada, EventoReservaCreada, ReservaCreadaPayload
from app.moduls.lists.infrastructure.schema.v1.commands import ComandoCrearReserva, ComandoCrearReservaPayload
from app.seedwork.infrastructure import utils
from pulsar.schema import JsonSchema, Record
import datetime
import logging

# Enable Pulsar client logging
logging.basicConfig(level=logging.DEBUG)
epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico)
        serialized_data = json.dumps(mensaje.data).encode('utf-8')       
        publicador.send(serialized_data)
        publicador.close()

    def publicar_evento(self, evento, topico):
        payload = ReservaCreadaPayload(
            id_reserva=str(evento.id_reserva), 
            id_cliente=str(evento.id_cliente), 
            estado=str(evento.estado), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = ComandoCrearReserva(data=payload)
        #self._publicar_mensaje(evento_integracion, topico, schema= AvroSchema(ComandoCrearReserva))

    def publicar_comando(self, comando, topico):
        self._publicar_mensaje(comando, topico)
