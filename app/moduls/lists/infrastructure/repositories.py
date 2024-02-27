""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de lists
"""

from app.config.db import SessionLocal
from .dto import Estate
from ..aplication.dto import EstateDTO
from ..domain.repositories import ListRepository


class EstateRepositoryPostgres(ListRepository):

    def get_by_id(self, entity_id: int) -> Estate:
        # TODO
        raise NotImplementedError

    def get_all(self) -> list[EstateDTO]:
        db = SessionLocal()
        reserva_dto = db.query(Estate).all()
        estate_list = [EstateDTO(id=item.id, code=item.code, name=item.name) for item in reserva_dto]
        return estate_list

    def create(self, entity: Estate):
        # TODO
        raise NotImplementedError

    def update(self, entity_id: int, entity: Estate):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: int):
        # TODO
        raise NotImplementedError
