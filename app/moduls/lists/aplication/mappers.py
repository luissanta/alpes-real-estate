from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.lists.domain.entities import Estate
from app.moduls.lists.domain.value_objects import Code, Name
from .dto import EstateDTO

from datetime import datetime

class MapeadorEstateDTOJson(AppMap):
    def _procesar_estate(self, estate: dict) -> EstateDTO:

        estate_dto: EstateDTO = EstateDTO(estate.get('id'), estate.get('code'), estate.get('name')) 
        return estate_dto
    
    def external_to_dto(self, externo: dict) -> EstateDTO:
        estate_dto: EstateDTO = EstateDTO(externo.get('id'), externo.get('code'), externo.get('name')) 
        return estate_dto

    def dto_to_external(self, dto: EstateDTO) -> dict:
        return dto#.__dict__

class MapeadorEstate(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def _procesar_itinerario(self, estate_dto: EstateDTO) -> Estate:
        return Estate(estate_dto.id, estate_dto.code, estate_dto.name)

    def get_type(self) -> type:
        return Estate.__class__

    def entity_to_dto(self, entidad: Estate) -> EstateDTO:
        return EstateDTO(entidad.id, entidad.code, entidad.name)

    def dto_to_entity(self, dto: EstateDTO) -> Estate:
        print("dto_to_entity")
        print(dto)

        return [Estate(code= dto.code, name= dto.name) for dto in dto]
    
