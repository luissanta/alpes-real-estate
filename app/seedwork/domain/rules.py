"""Reglas de negocio reusables parte del seedwork del proyecto
En este archivo usted encontrará reglas de negocio reusables parte del seedwork del proyecto
"""
from abc import ABC, abstractmethod


class BusinessRule(ABC):
    __message: str = 'La regla de negocio es invalida'

    def __init__(self, message):
        self.__message = message

    def message_error(self) -> str:
        return self.__message

    @abstractmethod
    def is_valid(self) -> bool:
        ...

    def __str__(self):
        return f"{self.__class__.__name__} - {self.__message}"

class IdEntidadEsInmutable(BusinessRule):

    entity: object

    def __init__(self, entity, mensaje='El identificador de la entidad debe ser Inmutable'):
        super().__init__(mensaje)
        self.entity = entity

    def is_valid(self) -> bool:
        try:
            if self.entity._id:
                return False
        except AttributeError as error:
            return True
