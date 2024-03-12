import uuid
from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.locations.domain.entities import Location, List_locations
from app.moduls.locations.domain.value_objects import Code, Name
from .dto import Location as LocationDTO ,List_locations as List_locationsDTO

from datetime import datetime
class MapeadorLocation(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_locations(self, list_location: List_locations) -> LocationDTO:
<<<<<<< HEAD
        return [LocationDTO(location_id=str(item.id), code=item.code, name=item.name) for item in list_location]
=======
        return [LocationDTO(location_id=str(item.id), code=item.code, name=item.name, uniquecode = str(uuid.uuid4())) for item in list_location]
>>>>>>> develop
    
    def _procesar_locations_dto(self, list_location_dto: List_locationsDTO) -> Location:
        return [Location(location_id=str(item.id), code=item.code, name=item.name) for item in list_location_dto]

    def get_type(self) -> type:
        return List_locations.__class__

    def entity_to_dto(self, list_entidad: List_locations) -> List_locationsDTO:
        list_dto = List_locationsDTO()
        list_dto.locations = list()

        if not list_entidad:
            return list_dto

        list_dto.id = str(uuid.uuid4())
        list_dto.createdAt = datetime.now()
        list_dto.updatedAt = datetime.now()

        locations_entity: list[Location] = list_entidad.locations

        list_dto.locations.extend(self._procesar_locations(locations_entity))

        return list_dto

    def dto_to_entity(self, dto: List_locationsDTO) -> List_locations:
        list_locations = List_locations()
        list_locations.locations = list()
        if not dto:
            return list_locations
        
        list_locations.createdAt = datetime.now()
        list_locations.updatedAt = datetime.now()

        estates_dto: list[LocationDTO] = dto.locations

        list_locations.locations.extend(self._procesar_locations_dto(estates_dto))

        return list_locations