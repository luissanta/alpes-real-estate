""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from app.seedwork.domain.repositories import Mapper
from app.moduls.lists.domain.value_objects import Name, Code
from app.moduls.lists.domain.entities import Estate, EstateList
from ..infrastructure.dto import Estate as EstateDTO


class MapperListEstates(Mapper):
    def get_type(self) -> type:
        return Estate.__class__
        pass

    def _create_estate_dto(self, dto: EstateDTO) -> Estate:
        estate = Estate(code=dto.code, name=dto.name)
        return estate

    def _create_lists_estate_dto(self, lists_dto: list[EstateDTO]) -> list[Estate]:
        estates = []
        for dto in lists_dto:
            estate = self._create_estate_dto(dto)
            estates.append(estate)
        return estates

    def dto_to_entity(self, dto: EstateDTO) -> Estate:
        estate = self._create_estate_dto(dto)
        estate_list = EstateList(estate_id=dto.id)
        estate_list.estates.extend(self._create_lists_estate_dto([estate]))
        return estate_list

    def entity_to_dto(self, estate: Estate) -> EstateDTO:
        return self._create_estate_dto(estate)
