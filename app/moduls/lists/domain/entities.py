"""Entidades del dominio de lists

En este archivo usted encontrará las entidades del dominio de lists
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import uuid
from app.moduls.lists.domain.events import ReservaCreada
import app.moduls.lists.domain.value_objects as ov
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class Estate(Entity):    
    code: str = field(default_factory=str)
    name: str = field(default_factory=str)
    # createdAt: str = field(default_factory=str)
    # updatedAt: str = field(default_factory=str)

@dataclass
class List_estates(RootAggregation):
    id: str = field(hash=True, default=None)
    estates: list[Estate] = field(default_factory=list)
    created_at: datetime = field(default=datetime.now())
    updated_at: datetime = field(default=datetime.now())
       

    def create_estate(self, estateslist: List_estates):
        estates = estateslist
        # for estate in estateslist:
        #     self.estate.id = estate.id
        #     self.estate.code = estate.code
        #     self.estate.name = estate.name
        #     self.createdAt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        #     self.updatedAt = None #datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        
        #     self.estates.append(estate)
        self.add_events(ReservaCreada(id=1,id_reserva="1", id_cliente="1", estado="funciona", fecha_creacion=datetime.now()))