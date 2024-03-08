from pulsar.schema import *
from dataclasses import dataclass, field
from app.seedwork.infrastructure.schema.v1.comandos import ComandoIntegracion

class ComandoCrearReservaPayload(Record):
    id = String()
    locations = [{"code": String(), "name": String()}]
    # TODO Cree los records para itinerarios

#     class LocationRecord(Record):
#     code = String()
#     name = String()

class CommandCreateCompanyJson(Record):
     data = String()
#     locations = Array(LocationRecord) 

class ComandoCrearReserva(Record):
    data = ComandoCrearReservaPayload()

class CommandRollbackCreateCompanyJson(Record):
     data = String()