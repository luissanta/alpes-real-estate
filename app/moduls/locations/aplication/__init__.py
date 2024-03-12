from pydispatch import dispatcher

from .handlers import HandlerReservaDominio

from app.moduls.locations.domain.events import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada

dispatcher.connect(HandlerReservaDominio.handle_reserva_creada, signal='ComandoCrearReservaPayloadDominio')
#dispatcher.connect(HandlerReservaIntegracion.handle_reserva_creada, signal=f'{ReservaCreada.__name__}Integracion')
#handle_propiedad_vendida
#dispatcher.connect(HandlerReservaIntegracion.handle_reserva_cancelada, signal=f'{ReservaCancelada.__name__}Integracion')
#dispatcher.connect(HandlerReservaIntegracion.handle_reserva_pagada, signal=f'{ReservaPagada.__name__}Integracion')
#dispatcher.connect(HandlerReservaIntegracion.handle_reserva_aprobada, signal=f'{ReservaAprobada.__name__}Integracion')
#dispatcher.connect(HandlerReservaDominio.handle_reserva_creada, signal='ComandoCrearReservaPayloadDominio')