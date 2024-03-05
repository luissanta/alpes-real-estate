from pulsar.schema import *
from dataclasses import dataclass, field
from app.seedwork.infrastructure.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearLocationPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearLocation(ComandoIntegracion):
    data = ComandoCrearLocationPayload()