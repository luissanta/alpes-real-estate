import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from app.moduls.lists.infrastructure.schema.v1.events import EventoReservaCreada
from app.moduls.locations.aplication.commands.create_location import CreateEstateHandler, CreateLocation

from app.moduls.locations.infrastructure.schema.v1.events import EventoLocationCreada
from app.moduls.locations.infrastructure.schema.v1.commands import ComandoCrearLocation
from app.seedwork.aplication.commands import execute_command
from app.seedwork.infrastructure import utils
from app.moduls.locations.aplication.mappers import MapeadorEstateDTOJson as MapApp

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-reserva-dominio', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(EventoReservaCreada))

        while True:
            mensaje = consumidor.receive()

            print(f'Evento procesado correctamente: {mensaje.value().data}')
            execute_event_domain(mensaje.value().data)
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def execute_event_domain(message):
    try:
        estate_dict = message

        #print("Request.json: ", estate_dict)
        map_estate = MapApp()
        estate_dto = map_estate.external_pulsar_to_dto(estate_dict)

        command = CreateLocation(estate_dto)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        execute_command(command)
        return print("Evento procesado correctamente")
    except Exception as e:
        return print("Evento procesado correctamente", e)

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-reserva-dominio', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aeroalpes-sub-comandos', schema=AvroSchema(ComandoCrearLocation))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()