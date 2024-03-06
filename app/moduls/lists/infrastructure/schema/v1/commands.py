from pulsar.schema import *
from dataclasses import dataclass, field
from app.seedwork.infrastructure.schema.v1.comandos import ComandoIntegracion

class ComandoCrearReservaPayload(ComandoIntegracion):
    id = String()
    locations = [{"code": String(), "name": String()}]
    # TODO Cree los records para itinerarios

class ComandoCrearReserva(ComandoIntegracion):
    data = ComandoCrearReservaPayload()