from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from app.seedwork.domain.events import (DomainEvent)
from datetime import datetime

class EventoReserva(DomainEvent):
    ...

@dataclass
class ReservaCreada(EventoReserva):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    
@dataclass
class ReservaCancelada(EventoReserva):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ReservaAprobada(EventoReserva):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ReservaPagada(EventoReserva):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None