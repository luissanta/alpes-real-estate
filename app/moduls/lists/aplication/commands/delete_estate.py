from app.seedwork.aplication.commands import Command
from app.moduls.lists.aplication.dto import ListDTO
from .base import CreateEstateBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplication.commands import execute_command as command

from app.moduls.lists.domain.entities import Estate
from app.seedwork.infrastructure.uow import UnitOfWorkPort
from app.moduls.lists.aplication.mappers import MapeadorEstate
from app.moduls.lists.infrastructure.repositories import ListRepository

@dataclass
class DeleteEstate(Command):
    id: str

class DeleteEstateHandler(CreateEstateBaseHandler):
    
    def handle(self, command: DeleteEstate):
        id_list_estate = command

        repository = self.repository_factory.create_object(ListRepository.__class__)

        UnitOfWorkPort.regist_batch(repository.delete, id_list_estate)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()


@command.register(DeleteEstate)
def execute_command_delete_state(comando: DeleteEstate):
    handler = DeleteEstateHandler()
    handler.handle(comando)
    