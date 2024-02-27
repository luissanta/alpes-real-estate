""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de lists
"""

from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from app.seedwork.domain.repositories import Repository
from .exceptions import FactoryException
from .repositories import EstateRepositoryPostgres
from ..domain.repositories import ListRepository


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == ListRepository.__class__:
            return EstateRepositoryPostgres()
        else:
            raise FactoryException
