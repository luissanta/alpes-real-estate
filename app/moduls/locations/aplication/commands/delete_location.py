from app.seedwork.aplication.commands import Command
from app.moduls.locations.aplication.dto import ListDTO
from .base import CreateLocationBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplication.commands import execute_command as command

from app.moduls.locations.domain.entities import Location
from app.seedwork.infrastructure.uow import UnitOfWorkPort
from app.moduls.locations.aplication.mappers import MapeadorLocation
from app.moduls.locations.infrastructure.repositories import ListRepository

@dataclass
class DeleteLocation(Command):
    id: str

class DeleteLocationHandler(CreateLocationBaseHandler):
    
    def handle(self, command: DeleteLocation):
        id_location_estate = command
        
        repository = self.repository_factory.create_object(ListRepository.__class__)

        UnitOfWorkPort.regist_batch(repository.delete, id_location_estate)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()


@command.register(DeleteLocation)
def execute_command_create_state(comando: DeleteLocation):
    handler = DeleteLocationHandler()
    handler.handle(comando)