import pulsar
from pulsar.schema import *

from app.moduls.locations.infrastructure.schema.v1.events import EventoLocationCreada, LocationCreadaPayload
from app.moduls.locations.infrastructure.schema.v1.commands import ComandoCrearLocation, ComandoCrearLocationPayload
from app.seedwork.infrastructure import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoLocationCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = LocationCreadaPayload(
            id_reserva=str(evento.id_reserva), 
            id_cliente=str(evento.id_cliente), 
            estado=str(evento.estado), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoLocationCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoLocationCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearLocationPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearLocation(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearLocation))

