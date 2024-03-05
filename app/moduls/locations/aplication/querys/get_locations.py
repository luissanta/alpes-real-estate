from app.seedwork.aplication.queries import Query, QueryHandler, QueryResultado
from app.seedwork.aplication.queries import execute_query as query
from app.moduls.locations.infrastructure.repositories import ListRepository
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from app.moduls.locations.aplication.mappers import MapeadorLocation
import uuid

@dataclass
class GetLocation(Query):
    id: str

class getEstatesHandler(ReservaQueryBaseHandler):
    def handle(self, query: GetLocation
) -> QueryResultado:
        repositorio = self._repository_factory.create_object(ListRepository.__class__)
        reserva =  self._list_factories.create_object(repositorio.get_all(), MapeadorLocation())
        return QueryResultado(resultado=reserva)

@query.register(GetLocation)
def execute_query_get_list(query: GetLocation):
    handler = getEstatesHandler()
    return handler.handle(query)