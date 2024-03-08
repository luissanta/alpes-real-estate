"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de locations
"""

from app.seedwork.domain.rules import BusinessRule
from .entities import Location


class EstateMinOne(BusinessRule):

    locations: list[Location]

    def __init__(self, locations, mensaje='Al menos una lacalidad debe estar en el listado'):
        super().__init__(mensaje)
        self.locations = locations

    def is_valid(self) -> bool:
        for locations in self.locations:
            if locations.code == Location.code:
                return True
        return False
