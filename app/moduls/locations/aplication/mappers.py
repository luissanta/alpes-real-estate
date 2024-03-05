from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.locations.domain.entities import Location, List_locations
from app.moduls.locations.domain.value_objects import Code, Name
from .dto import LocationDTO, ListDTO

from datetime import datetime

class MapeadorEstateDTOJson(AppMap):
    def _procesar_estate(self, location: dict) -> LocationDTO:

        estate_dto: LocationDTO = LocationDTO( location.get('code'), location.get('name')) 
        return estate_dto
    
    def _procesar_pulsar_estate(self, location:any) -> LocationDTO:

        estate_dto: LocationDTO = LocationDTO( location.id_cliente, location.estado) 
        return estate_dto
    
    def external_to_dto(self, externo: dict) -> ListDTO:

        list_dto = ListDTO()

        locations: list[LocationDTO] = list()
        for itin in externo.get("locations"):
            list_dto.locations.append(self._procesar_estate(itin))

        return list_dto
    
    def external_pulsar_to_dto(self, externo) -> ListDTO:

        list_dto = ListDTO()

        locations: list[LocationDTO] = list()
       
        
        list_dto.locations.append(self._procesar_pulsar_estate(externo))

        return list_dto

    def dto_to_external(self, dto: ListDTO) -> dict:
        return dto.__dict__

class MapeadorLocation(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def _procesar_locations(self, estate_dto: LocationDTO) -> Location:
        return Location(code=estate_dto.code, name=estate_dto.name)
    
    def get_type(self) -> type:
        return Location.__class__

    def entity_to_dto(self, list_entidad: List_locations) -> ListDTO:
        list_dto = ListDTO()

        for locations_entity in list_entidad.locations:
            estate_dto = LocationDTO(id=locations_entity.id, name=locations_entity.name, code=locations_entity.code)
            list_dto.locations.append(estate_dto) 

        return list_dto

    def dto_to_entity(self, dto: ListDTO) -> List_locations:
        list_locations = List_locations()
        list_locations.locations = list()

        estates_dto: list[LocationDTO] = dto.locations

        for itin in estates_dto.locations:
            list_locations.locations.append(self._procesar_locations(itin))
            
        return list_locations