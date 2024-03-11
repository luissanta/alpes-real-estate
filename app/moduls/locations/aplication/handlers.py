import pickle
from app.moduls.lists.infrastructure.schema.v1.events import  CommandResponseCreateEstateJson, CommandResponseCreateEstateJsonPayload, CommandResponseRollbackCreateEstateJson, CustomPayload, EventoCustom
from app.moduls.locations.domain.events import ReservaCreada
from app.moduls.locations.infrastructure.dispachers import Despachador
from app.seedwork.aplication.handlers import Handler
from app.moduls.locations.aplication.mappers import MapeadorEstateDTOJson as MapApp
from app.moduls.locations.aplication.commands.create_location import CreateEstateHandler, CreateLocation
from app.seedwork.aplication.commands import execute_command
from pulsar.schema import *
import json
from datetime import datetime
from uuid import UUID
from app.moduls.lists.infrastructure.schema.v1.commands import ComandoCrearReserva, ComandoCrearReservaPayload


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        elif isinstance(obj, UUID):
            return str(obj)
        #elif isinstance(obj, Estate):
        #    return {'id': str(obj.id), 'createdAt': obj.createdAt, 'updatedAt': obj.updatedAt, 'code': obj.code, 'name': obj.name}
        elif isinstance(obj, ComandoCrearReservaPayload):
            return {'id': obj.id, 'locations': self.serialize_locations(obj.locations)}
        elif isinstance(obj, ComandoCrearReserva):
            return {'data': self.default(obj.data)}
        return super().default(obj)

    def serialize_locations(self, locations):
        # Assuming locations is a list of dictionaries
        serialized_locations = []
        for location in locations:
            serialized_location = {'code': location['code'], 'name': location['name']}
            serialized_locations.append(serialized_location)
        return serialized_locations

class HandlerReservaDominio(Handler):

    
    @staticmethod
    def handle_reserva_creada(evento):
        # Obtener los valores del objeto evento

        # Decodificar el mensaje utilizando el esquema Avro
        #value = schema.Schema.decode_message(evento.value())

        try:
            # Crear una instancia de AvroSchema con la clase de registro ComandoCrearReserva
           
            print('================ RESERVA CREADA ===========')
         
            valyue = pickle.loads(pickle.dumps(evento))
           
            map_estate = MapApp()
            estate_dto = map_estate.external_pulsar_to_dto(evento)

            command = CreateLocation(estate_dto)
            
            # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
            # Revise la clase Despachador de la capa de infraestructura
            execute_command(command)
            despachador = Despachador()
            command = CommandResponseCreateEstateJson()
            payload = CommandResponseCreateEstateJsonPayload() 
            payload.data = '{"id": "1", "name": "Estate 1", "code": "E1", "createdAt": "2021-08-01T00:00:00.000Z", "updatedAt": "2021-08-01T00:00:00.000Z"}'
            command.data = '{"id": "1", "name": "Estate 1", "code": "E1", "createdAt": "2021-08-01T00:00:00.000Z", "updatedAt": "2021-08-01T00:00:00.000Z"}'
            #command.data = "Evento procesado correctamente"   

            # Example with instance data
            evento_custom = EventoCustom(
                id="12345",
                time=1634567890,
                ingestion=1634567890,
                specversion="1.0",
                type="custom.event",
                datacontenttype="application/json",
                service_name="my-service",
                data=CustomPayload(
                    id_reserva="reserva-123",
                    id_cliente="cliente-456",
                    estado="activo",
                    fecha_creacion=1634567890
                )
            )

            despachador.publicar_comando_avro_response_estate(command, 'response-create-estate')
            return print("Evento procesado correctamente")
        except Exception as e:
            despachador = Despachador()
            command = CommandResponseRollbackCreateEstateJson()

            command.data = "Evento Fallido"               
            despachador.publicar_comando_avro_rollback_response_estate(command, 'response-rollback-create-estate')
            print(e)
            print('ERROR: Suscribiendose al tópico de comandos!')
            return print("Evento procesado correctamente", e)
        
    
        