from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.lists.domain.entities import Estate, GeoLocation, List_estates
from app.moduls.lists.domain.value_objects import Code, Name
from .dto import EstateDTO, GeoLocationDTO, ListDTO

from datetime import datetime

class MapeadorEstateDTOJson(AppMap):
    def _procesar_estate(self, estate: dict) -> EstateDTO:

        geo_locations_ext: list[GeoLocationDTO] = list()

        for itin in estate.get("location"):
            geo_locations_ext.append(self._procesar_geo_locations(itin))

        estate_dto: EstateDTO = EstateDTO( code=estate.get('code'), name=estate.get('name'), geo_locations=geo_locations_ext) 
        return estate_dto
    
    def _procesar_geo_locations(self, geo_location: dict) -> GeoLocationDTO:

        geo_location_dto: GeoLocationDTO = GeoLocationDTO( lat=geo_location.get('lat'), lon=geo_location.get('lon')) 
        return geo_location_dto
    
    def external_to_dto(self, externo: dict) -> ListDTO:

        list_dto = ListDTO()

        for itin in externo.get("estates"):
            list_dto.estates.append(self._procesar_estate(itin))

        return list_dto

    def dto_to_external(self, dto: ListDTO) -> dict:
        return dto.__dict__

class MapeadorEstate(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def _procesar_estates(self, estate_dto: EstateDTO) -> Estate:
        geo_locations_entity: list[GeoLocationDTO] = list()

        for itin in estate_dto.geo_locations:
            geo_locations_entity.append(self._procesar_geo_locations(itin))

        return Estate(code=estate_dto.code, name=estate_dto.name, geo_locations=geo_locations_entity)
    
    def _procesar_geo_locations(self, geo_location_dto: GeoLocationDTO) -> GeoLocation:
        return GeoLocation(lat=geo_location_dto.lat, lon=geo_location_dto.lon)
    
    def get_type(self) -> type:
        return Estate.__class__

    def entity_to_dto(self, list_entidad: List_estates) -> ListDTO:
        list_dto = ListDTO()
        geo_locations_dto: list[GeoLocationDTO] = list()

        for estates_entity in list_entidad.estates:
            for geo_location_entity in estates_entity.geo_locations:
                geo_locations_dto.append(GeoLocationDTO(lat=geo_location_entity.lat, lon=geo_location_entity.lon))

            estate_dto = EstateDTO(id=estates_entity.id, name=estates_entity.name, code=estates_entity.code)
            estate_dto.geo_locations = geo_locations_dto
            list_dto.estates.append(estate_dto) 

        return list_dto

    def dto_to_entity(self, dto: ListDTO) -> List_estates:
        list_estates = List_estates()
        list_estates.estates = list()

        estates_dto: list[EstateDTO] = dto.estates

        for itin in estates_dto.estates:
            list_estates.estates.append(self._procesar_estates(itin))
            
        return list_estates