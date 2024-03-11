from abc import ABC, abstractmethod
from app.moduls.lists.infrastructure.schema.v1.events import EventoIntegracion1
from app.seedwork.aplication.commands import Command
from app.seedwork.domain.events import DomainEvent
from dataclasses import dataclass, field
from .commands import execute_command
import uuid
import datetime

class CoordinadorSaga(ABC):
    id_correlacion: uuid.UUID

    @abstractmethod
    def persistir_en_saga_log(self, mensaje):
        ...

    @abstractmethod
    def construir_comando(self, evento: DomainEvent, tipo_comando: type) -> Command:
        ...

    def publicar_comando(self,evento: DomainEvent, tipo_comando: type):
        comando = self.construir_comando(evento, tipo_comando)
        execute_command(comando)
        

    @abstractmethod
    def inicializar_pasos(self):
        ...
    
    @abstractmethod
    def procesar_evento(self, evento: DomainEvent):
        ...

    @abstractmethod
    def iniciar(self):
        ...
    
    @abstractmethod
    def terminar(self, mensaje):
        ...

class Paso():
    id_correlacion: uuid.UUID
    fecha_evento: datetime.datetime
    index: int

@dataclass
class Inicio(Paso):
    index: int = 0

@dataclass
class Fin(Paso):
    index: int = 0

@dataclass
class Transaccion(Paso):
    
    comando: Command
    evento: EventoIntegracion1
    error: EventoIntegracion1
    compensacion: Command
    exitosa: bool
    index: int = field(default=0)

    def __init__(self, id_correlacion, fecha_evento, comando, evento, error, compensacion, exitosa, index=0):
        self.comando = comando
        self.evento = evento
        self.error = error
        self.compensacion = compensacion
        self.exitosa = exitosa
        self.id_correlacion = id_correlacion
        self.fecha_evento = fecha_evento
        self.index = index
        

class CoordinadorCoreografia(CoordinadorSaga, ABC):
    # TODO Piense como podemos hacer un Coordinador con coreografía y Sagas
    # Piense en como se tiene la clase Transaccion, donde se cuenta con un atributo de compensación
    # ¿Tal vez un manejo de tuplas o diccionarios?
    ...

class CoordinadorOrquestacion(CoordinadorSaga, ABC):
    pasos: list[Paso]
    index: int
    
    def obtener_paso_dado_un_evento(self, evento: DomainEvent):
        for i, paso in enumerate(self.pasos):
            if not isinstance(paso, Transaccion):
                continue

            if isinstance(evento, paso.evento) or isinstance(evento, paso.error):
                return paso, i
        raise Exception("Evento no hace parte de la transacción")
                
    def es_ultima_transaccion(self, index):
        return (len(self.pasos) - 2)==index

    def procesar_evento(self, evento: DomainEvent):
        paso, index = self.obtener_paso_dado_un_evento(evento)
        if index == 1:            
            self.persistir_en_saga_log(f"Index: {index-1} Inicio + IdCorrelation={self.pasos[index].id_correlacion}")
            self.persistir_en_saga_log(f"Index: {index} {self.pasos[index].comando.__name__} - Comando IdCorrelation={self.pasos[index].id_correlacion}")

        if self.es_ultima_transaccion(index) and not isinstance(evento, paso.error):
            self.terminar(f"Index: {index+1} Fin + IdCorrelation={self.pasos[index].id_correlacion}")
        elif isinstance(evento, paso.error):
            if index != 1:
                self.publicar_comando(evento, self.pasos[index-1].compensacion)
                self.persistir_en_saga_log(f"Index: {index} {self.pasos[index-1].compensacion.__name__} - Compensación IdCorrelation={self.pasos[index-1].id_correlacion}")
            else:
                self.persistir_en_saga_log(f"Index: {index} Fin - Compensación IdCorrelation={self.pasos[index].id_correlacion}")
        elif isinstance(evento, paso.evento):
            self.persistir_en_saga_log(f"Index: {index+1} {self.pasos[index+1].comando.__name__} - Comando IdCorrelation={self.pasos[index].id_correlacion}")
            self.publicar_comando(evento, self.pasos[index+1].comando)


