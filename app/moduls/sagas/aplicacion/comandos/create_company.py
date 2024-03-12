from app.moduls.lists.infrastructure.dispachers import Despachador
from app.seedwork.aplication.commands import Command
from app.moduls.lists.aplication.dto import ListDTO
#from .base import CreateEstateBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplication.commands import execute_command as command

from app.moduls.lists.domain.entities import Estate
from app.seedwork.aplication.handlers import Handler
from app.seedwork.infrastructure.uow import UnitOfWorkPort
from app.moduls.lists.aplication.mappers import MapeadorEstate
from app.moduls.lists.infrastructure.repositories import ListRepository

class EmptyClass:
    pass
@dataclass
class CommandCreateCompanyJson(Command):
    data: str = field(default_factory=str)

class CreatedEstateHandler(EmptyClass):
    
    def handle(self, command: CommandCreateCompanyJson):
        print("Create company")
        try:
            despachador = Despachador()
            despachador.publicar_comando(command, "create-company")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        # estates = command
        
        # estate_list: ListDTO = self.list_factories.create_object(estates, MapeadorEstate())
        # estate_list.create_estate(estate_list)
        # repository = self.repository_factory.create_object(ListRepository.__class__)

        # UnitOfWorkPort.regist_batch(repository.create, estate_list)
        # #UnitOfWorkPort.savepoint()
        # UnitOfWorkPort.commit()


@command.register(CommandCreateCompanyJson)
def execute_command_created_state(comando: CommandCreateCompanyJson):
    handler = CreatedEstateHandler()
    handler.handle(comando)
