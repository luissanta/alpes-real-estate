""" Repositorios para el manejo de persiEstateDTOstencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos
"""

from app.config.db import SessionLocal
from .dto import Estate as EstateDTO
from app.moduls.lists.domain.entities import Estate,EstateList
from ..domain.repositories import ListRepository


class EstateRepositoryPostgres(ListRepository):

    def get_by_id(self, id: int) -> Estate:
        # TODO
        raise NotImplementedError

    def get_all(self) -> list[Estate]:
        session = SessionLocal()
        estate_dto = session.query(EstateDTO).all()
        estate_list = [Estate(id=item.id, code=item.code, name=item.name) for item in estate_dto]
        return [estate_list]

    def create(self, entity: Estate):
        # TODO
        raise NotImplementedError

    def update(self, entity_id: int, entity: Estate):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: int):
        # TODO
        raise NotImplementedError
