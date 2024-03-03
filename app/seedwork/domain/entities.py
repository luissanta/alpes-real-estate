"""Entidades reusables parte del seedwork del proyecto

En este archivo usted encontrará las entidades reusables parte del seedwork del proyecto
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
import uuid
from app.seedwork.domain.events import DomainEvent
from app.seedwork.domain.exceptions import IdMustBeInmutableExcepcion
from app.seedwork.domain.rules import IdEntidadEsInmutable


@dataclass
class Entity:
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    createdAt: datetime = field(default=datetime.now())
    updatedAt: datetime = field(default=datetime.now())

    @classmethod
    def siguiente_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        if not IdEntidadEsInmutable(self).is_valid():
            raise IdMustBeInmutableExcepcion()
        self._id = self.siguiente_id()
        

@dataclass
class RootAggregation(Entity):
    events: List[DomainEvent] = field(default_factory=list)

    def add_events(self, event: DomainEvent):
        self.events.append(event)
    
    def clear_events(self):
        self.events = list()
