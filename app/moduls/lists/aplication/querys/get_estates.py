from app.seedwork.aplication.queries import Query, QueryHandler, QueryResultado
from app.seedwork.aplication.queries import execute_query as query
from app.moduls.lists.infrastructure.repositories import ListRepository
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from app.moduls.lists.aplication.mappers import MapeadorEstate
import uuid

@dataclass
class getEstates(Query):
    id: str

class getEstatesHandler(ReservaQueryBaseHandler):

    def handle(self, query: getEstates) -> QueryResultado:
        repository = self._repository_factory.create_object(ListRepository.__class__)
        reserva =  self._list_factories.create_object(repository.get_all(), MapeadorEstate())        
        return QueryResultado(resultado=reserva)

@query.register(getEstates)
def exec_query_get_estates(query: getEstates):
    handler = getEstatesHandler()
    return handler.handle(query)