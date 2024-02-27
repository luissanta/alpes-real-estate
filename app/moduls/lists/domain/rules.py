"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de lists
"""

from app.seedwork.domain.rules import BusinessRule
from .entities import Estate


class EstateMinOne(BusinessRule):

    estates: list[Estate]

    def __init__(self, estates, mensaje='Al menos una propiedad debe estar en el listado'):
        super().__init__(mensaje)
        self.estates = estates

    def is_valid(self) -> bool:
        for estates in self.estates:
            if estates.code == Estate.code:
                return True
        return False
