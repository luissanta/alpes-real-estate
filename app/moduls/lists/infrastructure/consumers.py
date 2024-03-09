import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from app.moduls.lists.infrastructure.schema.v1.events import EventoReservaCreada
from app.seedwork.infrastructure import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-reserva', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(EventoReservaCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos_from_response_company():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('response-create-company', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='company-sub-commands')

        while True:
            mensaje = consumer.receive()
            print("Evento creacion ejecutado exitosamente id: {}".format(mensaje.data().decode('utf-8')))
            consumer.acknowledge(mensaje)     
            
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
    finally:
        if client:
            client.close()

def suscribirse_a_comandos_from_response_rollback_company():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('response-rollback-create-company', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='company-sub-commands')

        while True:
            mensaje = consumer.receive()
            print("Evento rollback ejecutado exitosamente id: {}".format(mensaje.data().decode('utf-8')))
            consumer.acknowledge(mensaje)     
            

    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
    finally:
        if client:
            client.close()

def suscribirse_a_comandos_from_response_audit():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('response-create-audit', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='audit-sub-commands')

        while True:
            mensaje = consumer.receive()
            print("Evento creacion ejecutado exitosamente id: {}".format(mensaje.data().decode('utf-8')))
            consumer.acknowledge(mensaje)     
            
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
    finally:
        if client:
            client.close()

def suscribirse_a_comandos_from_response_rollback_audit():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('response-rollback-create-audit', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='audit-sub-commands')

        while True:
            mensaje = consumer.receive()
            print("Evento rollback ejecutado exitosamente id: {}".format(mensaje.data().decode('utf-8')))
            consumer.acknowledge(mensaje)     
            

    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
    finally:
        if client:
            client.close()