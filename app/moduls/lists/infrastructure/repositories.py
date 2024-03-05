""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de lists
"""

from app.config.db import db
from app.moduls.lists.domain import factories
from .dto import List_estates as List_estatesDTO
from ..domain.entities import List_estates
from ..domain.repositories import ListRepository
from ..domain.factories import ListFactory
from ..infrastructure.mappers import MapeadorEstate


class EstateRepositoryPostgres(ListRepository):

    def __init__(self):
        self._estates_factory: ListFactory = ListFactory()

    @property
    def estates_factory(self):
        return self._estates_factory

    def get_by_id(self, entity_id: int) -> List_estates:
        # TODO
        list_estate_dto = db.session.query(List_estatesDTO).filter_by(id=str(entity_id)).one()
        try:    
            estate_list_entity = self.estates_factory.create_object(list_estate_dto, MapeadorEstate())             
        except Exception as e:
            print("Error: ", e)
        return estate_list_entity

    def get_all(self) -> list[List_estates]:
        list_estate_dto = db.session.query(List_estatesDTO).all()
        try:    
            estate_list_entity = self.estates_factory.create_object(list_estate_dto, MapeadorEstate()) 
            #[EstateDTO(id=item.id, code=item.code, name=item.name) for item in estate_dto]
        except Exception as e:
            print("Error: ", e)

        return estate_list_entity

    def create(self, entity: List_estates):
        # TODO
        listesates_dto = self.estates_factory.create_object(entity, MapeadorEstate())         
        db.session.add(listesates_dto)

    def update(self, entity_id: int, entity: List_estates):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: int):
        # TODO
        raise NotImplementedError
