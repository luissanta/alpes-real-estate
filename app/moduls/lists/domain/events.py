from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from app.seedwork.domain.events import (DomainEvent)
from datetime import datetime

@dataclass
class ReservaCreada(DomainEvent):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    
@dataclass
class ReservaCancelada(DomainEvent):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ReservaAprobada(DomainEvent):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ReservaPagada(DomainEvent):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None