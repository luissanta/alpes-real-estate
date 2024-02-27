from app.seedwork.aplication.queries import QueryHandler
from app.moduls.lists.infrastructure.factories import RepositoryFactory
from app.moduls.lists.domain.factories import ListFactory

class CreateEstateBaseHandler(QueryHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._list_factories: ListFactory = ListFactory()

    @property
    def fabrica_repositorio(self):
        return self._repository_factory
    
    @property
    def fabrica_vuelos(self):
        return self._list_factories    