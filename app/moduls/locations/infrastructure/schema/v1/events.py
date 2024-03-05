from pulsar.schema import *
from app.seedwork.infrastructure.schema.v1.eventos import EventoIntegracion

class LocationCreadaPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoLocationCreada(EventoIntegracion):
    data = LocationCreadaPayload()