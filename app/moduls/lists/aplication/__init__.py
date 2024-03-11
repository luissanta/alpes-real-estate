from pydispatch import dispatcher



from .handlers import HandlerReservaDominio, HandlerReservaIntegracion



#SI no funciona se debe habilidar dispatcher.connect(HandlerReservaDominio.handle_reserva_creada, signal=f'{ReservaCreada.__name__}Dominio')

#dispatcher.connect(HandlerReservaIntegracion.handle_compania_creada, signal=f'{CommandCreateCompanyJson.__name__}Integracion')
#dispatcher.connect(HandlerReservaIntegracion.handle_rollback_compania_creada, signal=f'{CommandRollbackCreateCompanyJson.__name__}Integracion')

#dispatcher.connect(HandlerReservaIntegracion.handle_auditoria_creada, signal=f'{CommandCreateAuditJson.__name__}Integracion')
#dispatcher.connect(HandlerReservaIntegracion.handle_rollback_auditoria_creada, signal=f'{CommandRollbackCreateAuditJson.__name__}Integracion')


#dispatcher.connect(HandlerReservaIntegracion.handle_rollback_Estate_creada, signal=f'{CommandRollbackCreateEstateJson.__name__}Integracion')

dispatcher.connect(HandlerReservaDominio.handle_created_estate, signal='CreatedEstateDominio')