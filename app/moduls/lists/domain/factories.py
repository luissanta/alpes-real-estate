""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de lists
"""

from app.moduls.lists.domain.exceptions import ObjectTypeNotExistInEstatesDomainException
from app.moduls.lists.domain.rules import EstateMinOne
from app.seedwork.domain.repositories import Mapper
from app.seedwork.domain.factories import Factory
from .entities import Estate, Entity
from dataclasses import dataclass



@dataclass
class _FabricaListado(Factory):
    def crear_objeto(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to__dto(obj)
        else:
            reserva: list = mapper.dto_to_entity(obj)

            self.validate_rule(EstateMinOne(Estate.code))

            return reserva


@dataclass
class ListFactory(Factory):
    def create_object(self, obj: type, mapper: Mapper = None) -> any:
        if mapper.get_type(self) == Estate.__class__:
            fabrica_reserva = _FabricaListado()
            return fabrica_reserva.create_object(obj, mapper)
        else:
            raise ObjectTypeNotExistInEstatesDomainException()
