from typing import Union
import uuid
from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.lists.domain.entities import Estate, List_estates
from app.moduls.lists.domain.value_objects import Code, Name
from .dto import Estate as EstateDTO ,List_estates as List_estatesDTO

from datetime import datetime
class MapeadorEstate(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_estates(self, list_estate: List_estates) -> EstateDTO:
        return [EstateDTO( estate_id=str(uuid.uuid4()), code=item.code, name=item.name, uniquecode = str(uuid.uuid4())) for item in list_estate]
    
    def _procesar_estates_dto(self, list_estate_dto: List_estatesDTO) -> Estate:
        return [Estate(estate_id=item.estate_id,id=item.estate_id, code=item.code, name=item.name) for item in list_estate_dto]

    def get_type(self) -> type:
        return List_estates.__class__

    def entity_to_dto(self, list_entidad: List_estates) -> List_estatesDTO:
        list_dto = List_estatesDTO()
        list_dto.estates = list()

        if not list_entidad:
            return list_dto

        list_dto.id = str(uuid.uuid4())
        
        list_dto.createdAt = datetime.now()
        list_dto.updatedAt = datetime.now()

        estates_entity: list[Estate] = list_entidad.estates

        list_dto.estates.extend(self._procesar_estates(estates_entity))

        return list_dto

    def dto_to_entity(self, dto: Union[list[List_estatesDTO], List_estatesDTO]) -> Union[list[List_estates], List_estates]:
        list_estate_entities: list = []

        list_estates = List_estates()
        list_estates.estates = list()
        if not dto:
            return list_estates
        
        if isinstance(dto, List_estates):
            list_estates.id = dto.id
            list_estates._id = dto.id
            list_estates.createdAt = datetime.now()
            list_estates.updatedAt = datetime.now()

            estates_dto: list[EstateDTO] = dto.estates

            list_estates.estates.extend(self._procesar_estates_dto(estates_dto))
            return list_estates 
            
        else:
             
            for list_estate in dto:
                list_estate_entity = List_estates()

                list_estate_entity.id = list_estate.id
                list_estate_entity._id = list_estate.id
                
                list_estate_entity.createdAt = datetime.now()
                list_estate_entity.updatedAt = datetime.now()

                estates_dto: list[EstateDTO] = list_estate.estates

                list_estate_entity.estates.extend(self._procesar_estates_dto(estates_dto))
                list_estate_entities.append(list_estate_entity)

            return list_estate_entities                