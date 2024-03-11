import json
from app.moduls.sagas.aplicacion.coordinadores.saga_propiedad import oir_mensaje
import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from app.moduls.lists.infrastructure.schema.v1.events import CommandResponseCreateAuditJson, CommandResponseCreateCompanyJson, CommandResponseCreateEstateJson, CommandResponseRollbackCreateAuditJson, CommandResponseRollbackCreateCompanyJson, CommandResponseRollbackCreateEstateJson, EventoCustom, EventoReservaCreada
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
            print("Evento creacion ejecutado exitosamente")
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
                                    subscription_name='company-sub-commands', schema=AvroSchema(CommandResponseRollbackCreateCompanyJson))

        while True:
            mensaje = consumer.receive()
            oir_mensaje(mensaje.value())
            print("Evento rollback ejecutado exitosamente id: {}".format(mensaje.value().data))
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
            print("Evento audit ejecutado exitosamente id: {}".format(mensaje.value().data))
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
            print("Evento audit rollback ejecutado exitosamente id: {}".format(mensaje.value().data))
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
            print("Evento crear propiedad ejecutado exitosamente id: {}".format(mensaje.value().data))
            #print("Evento rollback ejecutado exitosamente id: {}".format(mensaje.data().decode('utf-8')))
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
            print("Evento rollback ejecutado exitosamente id: {}".format(mensaje.data().decode('utf-8')))
            consumer.acknowledge(mensaje)     
            

    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
    finally:
        if client:
            client.close()


def suscribirse_a_comandos_delete():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('compensation-rollback-create-estate', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='delete-sub-commands')

        while True:
            mensaje = consumer.receive()
            oir_mensaje(mensaje.value())
            print("Mensaje recibido: {}".format(mensaje.data().decode('utf-8')))
            # with app.app_context():
            #     db.create_all()
            #     print(f"Current app name: {app.name}")
            #     json_data = json.loads(mensaje.data().decode('utf-8'))
            #     id_value = json_data.get("id")

            #     db.session.query(Company).filter(Company.id == id_value).delete()
            #     db.session.commit()
            #     db.session.close()

                # despachador = Despachador()
                # command = CommandResponseRollbackCreateCompanyJson()
                
                # command.data = id_value               
                # despachador.publicar_comando(command, 'response-rollback-create-company')

            consumer.acknowledge(mensaje)
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
    finally:
        if client:
            client.close()