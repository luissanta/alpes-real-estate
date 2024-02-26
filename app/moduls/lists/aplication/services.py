from app.seedwork.aplication.services import Service
from .dto import ListDTO
from app.moduls.lists.domain.factories import ListFactory
from app.moduls.lists.infrastructure.factories import RepositoryFactory
from ..domain.repositories import ListRepository
from .mappers import MapperListEstates


class ListService(Service):

    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._list_factories: ListFactory = ListFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def list_factory(self):
        return self._list_factories

    def get_list_by_id(self) -> ListDTO:
        repository = self.repository_factory.create_object(
            MapperListEstates)
        return repository.get_all()
