"""Entidades del dominio de locations

En este archivo usted encontrará las entidades del dominio de locations
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import uuid
from app.moduls.locations.domain.events import ReservaCreada
import app.moduls.locations.domain.value_objects as ov
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class Location(Entity):    
    code: str = field(default_factory=str)
    name: str = field(default_factory=str)
    # createdAt: str = field(default_factory=str)
    # updatedAt: str = field(default_factory=str)

@dataclass
class List_locations(RootAggregation):
    id: str = field(hash=True, default=None)
    locations: list[Location] = field(default_factory=list)
    created_at: datetime = field(default=datetime.now())
    updated_at: datetime = field(default=datetime.now())
       

    def create_location(self, locationslist: List_locations):
        locations = locationslist
        # for location in locationslist:
        #     self.location.id = location.id
        #     self.location.code = location.code
        #     self.location.name = location.name
        #     self.createdAt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        #     self.updatedAt = None #datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        
        #     self.locations.append(location)
        #self.add_events(ReservaCreada(id=1,id_reserva="1", id_cliente="1", estado="funciona", fecha_creacion=datetime.now()))