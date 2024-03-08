from pulsar.schema import *
from app.seedwork.infrastructure.schema.v1.eventos import EventoDominio, EventoIntegracion

class ReservaCreadaPayload(Record):
    id = String()
    estates = [{"code": String(), "name": String()}]



class EventoReservaCreada(EventoIntegracion):
    data = ReservaCreadaPayload()

class EventoDominioReservaCreada(EventoDominio):
    data = ReservaCreadaPayload()