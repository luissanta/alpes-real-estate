from pulsar.schema import *
from dataclasses import dataclass, field
from app.seedwork.infrastructure.schema.v1.comandos import ComandoIntegracion

class ComandoCrearReservaPayload(Record):
    id = String()
    locations = [{"code": String(), "name": String()}]
    # TODO Cree los records para itinerarios

class ComandoCrearReserva(Record):
    data = ComandoCrearReservaPayload()

class CommandCreateCompanyJson(Record):
     data = String()
    
class CommandRollbackCreateCompanyJson(Record):
     data = String()

class CommandCreateAuditJson(Record):
     data = String()
    
class CommandRollbackCreateAuditJson(Record):
     data = String()