""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de lists
"""

from app.moduls.lists.domain.exceptions import ObjectTypeNotExistInEstatesDomainException
from app.seedwork.domain.repositories import Mapper
from app.seedwork.domain.factories import Factory
from .entities import Estate, Entity
from dataclasses import dataclass


@dataclass
class _FabricaListado(Factory):
    def create_object(self, obj: any, mapper: Mapper = None) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            estate_list: Estate = mapper.dto_to_entity(obj)

            # self.validate_rule(EstateMinOne(Estate))

            return estate_list


@dataclass
class ListFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper = None) -> any:
        if mapper.get_type() == Estate.__class__:
            fabrica_reserva = _FabricaListado()
            return fabrica_reserva.create_object(obj, mapper)
        else:
            raise ObjectTypeNotExistInEstatesDomainException()

