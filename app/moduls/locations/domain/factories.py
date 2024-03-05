""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de locations
"""

from app.moduls.locations.domain.exceptions import ObjectTypeNotExistInEstatesDomainException
from app.moduls.locations.domain.rules import EstateMinOne
from app.seedwork.domain.repositories import Mapper
from app.seedwork.domain.entities import Entity
from .entities import Location, List_locations
from dataclasses import dataclass
from app.seedwork.domain.factories import Factory


@dataclass
class _ListFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper = None) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            list_locations: List_locations = mapper.dto_to_entity(obj)

            #self.validate_rule(EstateMinOne(Location.code))

            return list_locations


@dataclass
class ListFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper = None) -> any:
        if mapper.get_type() == Location.__class__:
            list_factory = _ListFactory()
            return list_factory.create_object(obj, mapper)
        else:
            raise ObjectTypeNotExistInEstatesDomainException()
