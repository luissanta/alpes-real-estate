import json
from app.moduls.lists.aplication.commands.delete_estate import DeleteEstate
from app.moduls.sagas.aplicacion.coordinadores.saga_propiedad import oir_mensaje
import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from app.moduls.lists.infrastructure.schema.v1.events import CommandResponseCreateAuditJson, CommandResponseCreateCompanyJson, CommandResponseCreateEstateJson, CommandResponseRollbackCreateAuditJson, CommandResponseRollbackCreateCompanyJson, CommandResponseRollbackCreateEstateJson, EventoCustom, EventoReservaCreada
from app.seedwork.aplication.commands import execute_command
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
                                    subscription_name='company-sub-commands', schema=AvroSchema(CommandResponseCreateCompanyJson))

        while True:
            mensaje = consumer.receive()
            oir_mensaje(mensaje.value())
            #print("Evento creacion ejecutado exitosamente id: {}".format(mensaje.data().decode('utf-8')))
            print("Evento response-create-company ejecutado exitosamente id: {}".format(mensaje.value().data))
            print("Evento creacion ejecutado exitosamente")
            consumer.acknowledge(mensaje)     
            
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
    finally:
        if client:
            client.close()

def suscribirse_a_comandos_from_response_rollback_company(app):
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('response-rollback-create-company', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='company-sub-commands', schema=AvroSchema(CommandResponseRollbackCreateCompanyJson))

        while True:
            mensaje = consumer.receive()
            with app.test_request_context():
                oir_mensaje(mensaje.value())
                print("Evento response-rollback-create-company ejecutado exitosamente id: {}".format(mensaje.value().data))
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
                                    subscription_name='audit-sub-commands', schema=AvroSchema(CommandResponseCreateAuditJson))

        while True:
            mensaje = consumer.receive()
            oir_mensaje(mensaje.value())
            print("Evento response-create-audit ejecutado exitosamente id: {}".format(mensaje.value().data))
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
                                    subscription_name='audit-sub-commands', schema=AvroSchema(CommandResponseRollbackCreateAuditJson))

        while True:
            mensaje = consumer.receive()            
            oir_mensaje(mensaje.value())
            print("Evento 'response-rollback-create-audit ejecutado exitosamente id: {}".format(mensaje.value().data))
            consumer.acknowledge(mensaje)     
            

    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
    finally:
        if client:
            client.close()
            
def suscribirse_a_comandos_from_response_create_estate():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('response-create-estate', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='estate-sub-commands', schema=AvroSchema(CommandResponseCreateEstateJson))#EventoCustom))#CommandResponseCreateEstateJson))
        while True:
            mensaje = consumer.receive()
            
            test = CommandResponseCreateEstateJson()
            test.data = "hola"
            oir_mensaje(mensaje.value())
            print("Evento response-create-estate ejecutado exitosamente id: {}".format(mensaje.value().data))
            consumer.acknowledge(mensaje)     
            

    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
    finally:
        if client:
            client.close()

def suscribirse_a_comandos_from_response_rollback_estate():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('response-rollback-create-estate', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='estate-sub-commands', schema=AvroSchema(CommandResponseRollbackCreateEstateJson))

        while True:
            mensaje = consumer.receive()
            oir_mensaje(mensaje.value())
            #oir_mensaje(mensaje)
            print("Evento response-rollback-create-estate ejecutado exitosamente id: {}".format(mensaje.value().data))
            consumer.acknowledge(mensaje)     
            

    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
    finally:
        if client:
            client.close()


def suscribirse_a_comandos_delete(app):
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('compensation-rollback-create-estate', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='delete-sub-commands')

        while True:
            mensaje = consumer.receive()
            with app.test_request_context():
                
                oir_mensaje(mensaje.value())
                command = DeleteEstate(-1)
                execute_command(command)
            print("Evento compensation-rollback-create-estate ejecutado exitosamente id: {}".format(mensaje.value().data))

            consumer.acknowledge(mensaje)
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
    finally:
        if client:
            client.close()