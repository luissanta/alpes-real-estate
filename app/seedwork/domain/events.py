"""Entidades reusables parte del seedwork del proyecto

En este archivo usted encontrará las clases para eventos reusables parte del seedwork del proyecto
"""

from dataclasses import dataclass, field
from .rules import IdEntidadEsInmutable
from .exceptions import IdMustBeInmutableExcepcion
from datetime import datetime
import uuid


@dataclass
class DomainEvent:
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    fecha_evento: datetime =  field(default=datetime.now())


    @classmethod
    def siguiente_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        if not IdEntidadEsInmutable(self).es_valido():
            raise IdMustBeInmutableExcepcion()
        self._id = self.siguiente_id()
