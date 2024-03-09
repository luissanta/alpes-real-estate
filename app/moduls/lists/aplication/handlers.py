from app.moduls.lists.domain.events import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
from app.seedwork.aplication.handlers import Handler
from app.moduls.lists.infrastructure.dispachers import Despachador

class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_compania_creada(evento):
        despachador = Despachador()
        despachador.publicar_comando(evento, 'create-company')

    @staticmethod
    def handle_rollback_compania_creada(evento):
        despachador = Despachador()
        despachador.publicar_comando(evento, 'rollback-create-company')
    
    @staticmethod
    def handle_auditoria_creada(evento):
        despachador = Despachador()
        despachador.publicar_comando(evento, 'create-audit')

    @staticmethod
    def handle_rollback_auditoria_creada(evento):
        despachador = Despachador()
        despachador.publicar_comando(evento, 'rollback-create-audit')

        

    @staticmethod
    def handle_reserva_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

    @staticmethod
    def handle_reserva_aprobada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

    @staticmethod
    def handle_reserva_pagada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

class HandlerReservaDominio(Handler):

    @staticmethod
    def handle_reserva_creada(evento):
        despachador = Despachador()
        despachador.publicar_comando(evento, 'eventos-reserva-dominio')

    @staticmethod
    def handle_reserva_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva-dominio')

    @staticmethod
    def handle_reserva_aprobada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva-dominio')

    @staticmethod
    def handle_reserva_pagada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva-dominio')
