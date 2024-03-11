from app.moduls.lists.aplication.commands.create_estate import CreateEstate
from app.moduls.lists.infrastructure.schema.v1.events import CommandResponseCreateAuditJson, CommandResponseCreateCompanyJson, CommandResponseCreateEstateJson, CommandResponseRollbackCreateAuditJson, CommandResponseRollbackCreateCompanyJson, CommandResponseRollbackCreateEstateJson, EventoIntegracion1
from app.moduls.sagas.aplicacion.comandos.create_audit import CommandCreateAuditJson
from app.moduls.sagas.aplicacion.comandos.create_company import CommandCreateCompanyJson
from app.moduls.sagas.aplicacion.comandos.rollback_create_audit import CommandRollbackCreateAuditJson
from app.moduls.sagas.aplicacion.comandos.rollback_create_company import CommandRollbackCreateCompanyJson
from app.moduls.sagas.aplicacion.comandos.rollback_create_state import CommandRollbackCreateEstateJson
from app.seedwork.aplication.commands import Command

from app.seedwork.aplication.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from app.seedwork.domain.events import DomainEvent
from pulsar.schema import *
import pulsar
from app.seedwork.infrastructure.schema.v1.eventos import EventoDominio, EventoIntegracion
import uuid
from datetime import date

class CoordinadorReservas(CoordinadorOrquestacion):
    def __init__(self):
        self.inicializar_pasos()

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, id_correlacion=str(uuid.uuid4()), exitosa=True, fecha_evento=date.today(), comando=CreateEstate, evento=CommandResponseCreateEstateJson, error=CommandResponseRollbackCreateEstateJson, compensacion=CommandRollbackCreateEstateJson),
            Transaccion(index=2, id_correlacion=str(uuid.uuid4()), exitosa=True, fecha_evento=date.today(),comando=CommandCreateCompanyJson, evento=CommandResponseCreateCompanyJson, error=CommandResponseRollbackCreateCompanyJson, compensacion=CommandRollbackCreateCompanyJson),
            Transaccion(index=3,  id_correlacion=str(uuid.uuid4()), exitosa=True,fecha_evento=date.today(),comando=CommandCreateAuditJson, evento=CommandResponseCreateAuditJson, error=CommandResponseRollbackCreateAuditJson, compensacion=CommandRollbackCreateAuditJson),
            Fin(index=4)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self, mensaje):
        self.persistir_en_saga_log(mensaje)

    def persistir_en_saga_log(self, mensaje):
        print("Persistiendo en la base de datos")
        print("======================================================"+mensaje)
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...


    def construir_comando(self, evento: type, tipo_comando: type):
        print("Construyendo comando")
        print(evento)
        comando = tipo_comando()  # Create an instance of tipo_comando
        comando.data = evento.data  # Set attributes of comando using attributes of evento
        return comando
        # TODO Set attributes of comando using attributes of evento
        
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoIntegracion1):#pulsar.Message):
        coordinador = CoordinadorReservas()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
