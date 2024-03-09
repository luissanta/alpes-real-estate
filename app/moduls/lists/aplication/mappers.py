from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.lists.domain.entities import Companies, Estate, GeoLocation, List_estates
from app.moduls.lists.domain.value_objects import Code, Name
from .dto import CompaniesDTO, EstateDTO, GeoLocationDTO, ListDTO

from datetime import datetime

class MapeadorEstateDTOJson(AppMap):
    def _procesar_estate(self, estate: dict) -> EstateDTO:

        geo_locations_ext: list[GeoLocationDTO] = list()
        companies_ext: list[CompaniesDTO] = list()

        for itin in estate.get("location"):
            geo_locations_ext.append(self._procesar_geo_locations(itin))

        for itin in estate.get("companies"):
            companies_ext.append(self._procesar_companies(itin))    

        estate_dto: EstateDTO = EstateDTO( code=estate.get('code'), name=estate.get('name'), geo_locations=geo_locations_ext, companies=companies_ext) 
        return estate_dto
    
    def _procesar_geo_locations(self, geo_location: dict) -> GeoLocationDTO:

        geo_location_dto: GeoLocationDTO = GeoLocationDTO( lat=geo_location.get('lat'), lon=geo_location.get('lon')) 
        return geo_location_dto
    
    def _procesar_companies(self, companies_dto: dict) -> CompaniesDTO:
        companies: CompaniesDTO = CompaniesDTO(company_name=companies_dto.get('company_name'), location=companies_dto.get('location'), typeCompany=companies_dto.get('typeCompany'))
        return companies
    
    def external_to_dto(self, externo: dict) -> ListDTO:

        list_dto = ListDTO()

        for itin in externo.get("estates"):
            list_dto.estates.append(self._procesar_estate(itin))

        return list_dto

    def dto_to_external(self, dto: ListDTO) -> dict:
        if isinstance(dto, ListDTO):
            return dto.__dict__
        return dto        

class MapeadorEstate(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_estates(self, estate_dto: EstateDTO) -> Estate:
        geo_locations_entity: list[GeoLocationDTO] = list()
        companies_entity: list[Companies] = list()

        for itin in estate_dto.geo_locations:
            geo_locations_entity.append(self._procesar_geo_locations(itin))

        for company in estate_dto.companies:
            companies_entity.append(self._procesar_companies(company))    

        return Estate( code=estate_dto.code, name=estate_dto.name, geo_locations=geo_locations_entity, companies = companies_entity)
    
    def _procesar_geo_locations(self, geo_location_dto: GeoLocationDTO) -> GeoLocation:
        return GeoLocation(lat=geo_location_dto.lat, lon=geo_location_dto.lon)
    
    def _procesar_companies(self, companies_dto: CompaniesDTO) -> Companies:
        return Companies(company_name=companies_dto.company_name, location=companies_dto.location, typeCompany=companies_dto.typeCompany)
    
    def get_type(self) -> type:
        return Estate.__class__

    def entity_to_dto(self, list_entidad: List_estates) -> ListDTO:
        list_dto = ListDTO()
        geo_locations_dto: list[GeoLocationDTO] = list()
        companies_dto: list[CompaniesDTO] = list()

        for estates_entity in list_entidad.estates:
            for geo_location_entity in estates_entity.geo_locations:
                geo_locations_dto.append(GeoLocationDTO(lat=geo_location_entity.lat, lon=geo_location_entity.lon))

            for company_entity in estates_entity.companies:
                companies_dto.append(CompaniesDTO(compay_name=company_entity.company_name, location=company_entity.location, typeCompany=company_entity.typeCompany))    

            estate_dto = EstateDTO(id=estates_entity.id, name=estates_entity.name, code=estates_entity.code)
            estate_dto.geo_locations = geo_locations_dto
            estate_dto.companies = companies_dto
            list_dto.estates.append(estate_dto) 

        return list_dto

    def dto_to_entity(self, dto: ListDTO) -> List_estates:
        list_estate_entities: list = []

        list_estates = List_estates()
        list_estates.estates = list()
        if not dto:
            return list_estates
        
        if isinstance(dto, list):

            for list_estate in dto:
                list_estate_entity = List_estates()
                list_estate_entity.createdAt = datetime.now()
                list_estate_entity.updatedAt = datetime.now()

                estates_dto: list[EstateDTO] = list_estate.estates

                for itin in estates_dto:
                    list_estates.estates.append(self._procesar_estates(itin))
                
                list_estate_entities.append(list_estates)

            return list_estate_entities    
        else:
            list_estates.createdAt = datetime.now()
            list_estates.updatedAt = datetime.now()

            estates_dto: list[EstateDTO] = dto.estates

            for itin in estates_dto.estates:
                list_estates.estates.append(self._procesar_estates(itin))

            return list_estates
            