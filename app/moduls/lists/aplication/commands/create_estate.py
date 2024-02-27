from app.seedwork.aplication.commands import Comando
from app.moduls.lists.aplication.dto import EstateDTO
from .base import CreateEstateBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplication.commands import ejecutar_commando as comando

from app.moduls.lists.domain.entities import Estate
from app.seedwork.infrastructure.uow import UnitOfWork
from app.moduls.lists.aplication.mappers import MapeadorReserva
from app.moduls.lists.infrastructure.repositories import ListRepository

@dataclass
class CreateEstate(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    estates: list[EstateDTO]


class CreateEstateHandler(CreateEstateBaseHandler):
    
    def handle(self, comando: CreateEstate):
        reserva_dto = EstateDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   itinerarios=comando.itinerarios)

        reserva: Estate = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())
        #reserva.crear_reserva(reserva)
        repositorio = self.fabrica_repositorio.crear_objeto(ListRepository.__class__)

        UnitOfWork.registrar_batch(repositorio.agregar, reserva)
        UnitOfWork.savepoint()
        UnitOfWork.commit()


@comando.register(CreateEstate)
def ejecutar_comando_crear_reserva(comando: CreateEstate):
    handler = CreateEstateHandler()
    handler.handle(comando)
    