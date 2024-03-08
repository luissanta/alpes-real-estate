""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de locations
"""

from app.config.db import db
from app.moduls.locations.domain import factories
from .dto import List_locations as List_locationsDTO
from ..domain.entities import List_locations
from ..domain.repositories import ListRepository
from ..domain.factories import ListFactory
from ..infrastructure.mappers import MapeadorLocation


class LocationRepositoryPostgres(ListRepository):

    def __init__(self):
        self._estates_factory: ListFactory = ListFactory()

    @property
    def locations_factory(self):
        return self._estates_factory

    def get_by_id(self, entity_id: int) -> List_locations:
        # TODO
        list_location_dto = db.session.query(List_locationsDTO).filter_by(id=str(entity_id)).one()
        try:    
            estate_list_entity = self.locations_factory.create_object(list_location_dto, MapeadorLocation())             
        except Exception as e:
            print("Error: ", e)
        return estate_list_entity

    def get_all(self) -> list[List_locations]:
        list_location_dto = db.session.query(List_locationsDTO).all()
        try:    
            estate_list_entity = self.locations_factory.create_object(list_location_dto, MapeadorLocation()) 
            #[LocationDTO(id=item.id, code=item.code, name=item.name) for item in estate_dto]
        except Exception as e:
            print("Error: ", e)

        return estate_list_entity

    def create(self, entity: List_locations):
        # TODO
        listesates_dto = self.locations_factory.create_object(entity, MapeadorLocation())         
        db.session.add(listesates_dto)

    def update(self, entity_id: int, entity: List_locations):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: int):
        # TODO
        raise NotImplementedError
