import uuid
from pulsar.schema import *
<<<<<<< HEAD
from app.seedwork.infrastructure.schema.v1.eventos import EventoDominio, EventoIntegracion
=======
from app.seedwork.domain.events import DomainEvent
from app.seedwork.infrastructure.schema.v1.eventos import EventoDominio, EventoIntegracion
from app.seedwork.infrastructure.schema.v1.mensajes import Mensaje
from app.seedwork.infrastructure.utils import time_millis
>>>>>>> develop

class ReservaCreadaPayload(Record):
    id = String()
    estates = [{"code": String(), "name": String()}]

class CreatedEstatePayload(Record):
    data = String()

class RollbackCreatedEstatePayload(Record):
    data = String()

class EventoReservaCreada(EventoIntegracion):
    data = ReservaCreadaPayload()

class EventoDominioReservaCreada(EventoDominio):
    data = ReservaCreadaPayload()

class CreatedEstate(EventoDominio):
    data = CreatedEstatePayload()

class RollbackCreatedEstate(EventoDominio):
    data = RollbackCreatedEstatePayload()

class Mensaje(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

    def __init__(self, *args, id=None, **kwargs):
        super().__init__(*args, id=id, **kwargs)


class EventoIntegracion1(Mensaje):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CommandResponseCreateAuditJson(EventoIntegracion1):
    data = String()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommandResponseCreateCompanyJson(EventoIntegracion1):
    data = String()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CommandResponseCreateEstateJsonPayload(Record):
    data = String()

class CommandResponseCreateEstateJson(EventoIntegracion1):
    data = String()#data = CommandResponseCreateEstateJsonPayload()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class CommandResponseRollbackCreateEstateJson(EventoIntegracion1):
    data = String()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class CommandResponseRollbackCreateCompanyJson(EventoIntegracion1):
    data = String()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CommandResponseRollbackCreateAuditJson(EventoIntegracion1):
    data = String()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CustomPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

<<<<<<< HEAD
class EventoReservaCreada(EventoIntegracion):
    data = ReservaCreadaPayload()

class EventoDominioReservaCreada(EventoDominio):
    data = ReservaCreadaPayload()
=======




class EventoCustom(EventoIntegracion1):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados, 
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = CustomPayload()



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
>>>>>>> develop
