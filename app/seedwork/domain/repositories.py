""" Interfaces para los repositorios reusables parte del seedwork del proyecto

En este archivo usted encontrará las diferentes interfaces para repositorios
reusables parte del seedwork del proyecto
"""

from abc import ABC, abstractmethod
from .entities import Entity


class Repository(ABC):
    @abstractmethod
    def get_by_id(self, entity_id: int) -> Entity:
        ...

    @abstractmethod
    def get_all(self) -> list[Entity]:
        ...

    @abstractmethod
    def create(self, entity: Entity):
        ...

    @abstractmethod
    def update(self, entity_id: int, entity: Entity):
        ...

    @abstractmethod
    def delete(self, entity_id: int):
        ...


class Mapper(ABC):
    @abstractmethod
    def get_type(self) -> type:
        ...

    @abstractmethod
    def entity_to_dto(self, entity: Entity) -> any:
        ...

    @abstractmethod
    def dto_to_entity(self, dto: any) -> Entity:
        ...
