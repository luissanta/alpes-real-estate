from pulsar.schema import *
from dataclasses import dataclass, field
from app.seedwork.infrastructure.schema.v1.comandos import ComandoIntegracion
from app.seedwork.aplication.commands import Command

class ComandoCrearReservaPayload(Record):
    data = String()
    id = String()
    locations = [{"code": String(), "name": String()}]
    # TODO Cree los records para itinerarios

class ComandoRollBackCreateEstatePayload(Record):
    data = String()
    id = String()
    locations = [{"code": String(), "name": String()}]
    # TODO Cree los records para itinerarios

class ComandoCrearReserva(Record):
    data = ComandoCrearReservaPayload()
