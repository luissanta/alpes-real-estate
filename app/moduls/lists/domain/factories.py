""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de lists
"""

from app.moduls.lists.domain.exceptions import ObjectTypeNotExistInEstatesDomainException
from app.moduls.lists.domain.rules import EstateMinOne
from app.seedwork.domain.repositories import Mapper
from .entities import Estate, Entity
from dataclasses import dataclass
from app.seedwork.domain.factories import Factory


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
    def create_object(self, obj: any, mapper: any = None) -> any:
        if isinstance(obj,Entity):
            fabrica_reserva = _FabricaListado()
            return fabrica_reserva.build_object(obj, mapper)
        else:
            print("entro por aqui")
            raise ObjectTypeNotExistInEstatesDomainException()
