from .mensajes import Mensaje
from dataclasses import dataclass
@dataclass
class EventoIntegracion(Mensaje):
    ...
@dataclass
class EventoDominio(Mensaje):
    ...