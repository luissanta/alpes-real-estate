from app.seedwork.aplication.commands import Command
from app.moduls.lists.aplication.dto import ListDTO
#from .base import CreateEstateBaseHandler
from dataclasses import dataclass, field


from app.moduls.lists.domain.entities import Estate
from app.seedwork.infrastructure.uow import UnitOfWorkPort
from app.moduls.lists.aplication.mappers import MapeadorEstate
from app.moduls.lists.infrastructure.repositories import ListRepository
from app.moduls.lists.aplication.commands.delete_estate import DeleteEstate
from app.seedwork.aplication.commands import execute_command
from app.seedwork.aplication.commands import execute_command as comando
class EmptyClass:
    pass

@dataclass
class CommandRollbackCreateEstateJson(Command):
    data: str = field(default_factory=str)

class CreatedEstateHandler(EmptyClass):
    
    def handle(self, command: CommandRollbackCreateEstateJson):
        estate_id = "07adc32e-885e-4768-95c2-bc876955f503"
        command = DeleteEstate(estate_id)
        execute_command(command)
        print("Rollback Create Estate")
        # estates = command
        
        # estate_list: ListDTO = self.list_factories.create_object(estates, MapeadorEstate())
        # estate_list.create_estate(estate_list)
        # repository = self.repository_factory.create_object(ListRepository.__class__)

        # UnitOfWorkPort.regist_batch(repository.create, estate_list)
        # #UnitOfWorkPort.savepoint()
        # UnitOfWorkPort.commit()


@comando.register(CommandRollbackCreateEstateJson)
def execute_command_created_state(comando: CommandRollbackCreateEstateJson):
    handler = CreatedEstateHandler()
    handler.handle(comando)
    