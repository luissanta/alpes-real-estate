"""Entidades del dominio de lists

En este archivo usted encontrará las entidades del dominio de lists
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import uuid
from app.moduls.lists.domain.events import ReservaCreada
import app.moduls.lists.domain.value_objects as ov
from app.moduls.lists.infrastructure.schema.v1.commands import ComandoCrearReserva, ComandoCrearReservaPayload
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class GeoLocation(Entity):    
    lat: str = field(default_factory=str)
    lon: str = field(default_factory=str)

@dataclass
class Estate(Entity):    
    code: str = field(default_factory=str)
    name: str = field(default_factory=str)
    geo_locations: list[GeoLocation] = field(default_factory=list[GeoLocation])
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
        cmd = ComandoCrearReservaPayload()
        cmd.id = estateslist.id
        for estate in estates:
            for geo_locations in estate.geo_locations:
                cmd.locations.append({"estate_id": id , "lat": geo_locations.lat, "lon": geo_locations.lon})
                self.add_events(cmd)    
            
            #cmd.locations.append({"code": estate.code, "name": estate.name})
            #elf.updatedAt = None #datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
            #self.add_events(ReservaCreada(id=estate.id,id_reserva=estate.id, id_cliente=estate.code, estado=estate.name, fecha_creacion=datetime.now()))
        #self.add_events(cmd)
        #self.add_events(cmd) #Add events for audit microservice
        
        