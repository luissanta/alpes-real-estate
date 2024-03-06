import json
import pulsar
from pulsar.schema import *

from app.moduls.lists.infrastructure.schema.v1.events import EventoDominioReservaCreada, EventoReservaCreada, ReservaCreadaPayload
from app.moduls.lists.infrastructure.schema.v1.commands import ComandoCrearReserva, ComandoCrearReservaPayload
from app.seedwork.infrastructure import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoReservaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ReservaCreadaPayload(
            id_reserva=str(evento.id_reserva), 
            id_cliente=str(evento.id_cliente), 
            estado=str(evento.estado), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoReservaCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoReservaCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        # payload = ComandoCrearReservaPayload(
        #     id = str(comando.id),
        #     locations=[
        #         {
        #             "code": "Intento 3",
        #             "name": "Intento 1 - Add your name in the body 1"
        #         },
        #         {
        #             "code": "Intento 3",
        #             "name": "Intento 2 - Add your name in the body 2"
        #         }
        #     ]
        # )
        # comando_integracion = ComandoCrearReserva(data=payload)
        # #self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearReserva))
        # cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        # publicador = cliente.create_producer(topico)
        # publicador.send(comando_integracion)
        # cliente.close()
        # Crear una instancia de ComandoCrearReservaPayload
        payload = ComandoCrearReservaPayload(
            id=str(comando.id),
            locations=[
                {"code": "Intento 3", "name": "Intento 1 - Add your name in the body 1"},
                {"code": "Intento 3", "name": "Intento 2 - Add your name in the body 2"}
            ]
        )

        # Convertir el objeto Python a una cadena JSON
        json_payload = json.dumps(payload.__dict__)

        # Configurar el cliente de Pulsar
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')

        # Configurar el productor
        
        publicador = cliente.create_producer(topico)

        # Enviar la cadena JSON como el contenido del mensaje
        publicador.send(json_payload)

        # Cerrar el cliente de Pulsar
        cliente.close()