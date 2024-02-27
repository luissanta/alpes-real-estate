from abc import ABC, abstractmethod
from enum import Enum

from app.seedwork.domain.entities import RootAggregation
#from pydispatch import dispatcher

import pickle


class Lock(Enum):
    OPTIMISTA = 1
    PESIMISTA = 2

class Batch:
    def __init__(self, operacion, lock: Lock, *args, **kwargs):
        self.operacion = operacion
        self.args = args
        self.lock = lock
        self.kwargs = kwargs

class UnitOfWork(ABC):

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def _obtener_eventos(self, batches=None):
        batches = self.batches if batches is None else batches
        for batch in batches:
            for arg in batch.args:
                if isinstance(arg, RootAggregation):
                    return arg.eventos
        return list()

    @abstractmethod
    def _limpiar_batches(self):
        raise NotImplementedError

    @abstractmethod
    def batches(self) -> list[Batch]:
        raise NotImplementedError

    @abstractmethod
    def savepoints(self) -> list:
        raise NotImplementedError                    

    def commit(self):
        self._publicar_eventos_post_commit()
        self._limpiar_batches()

    @abstractmethod
    def rollback(self, savepoint=None):
        self._limpiar_batches()
    
    @abstractmethod
    def savepoint(self):
        raise NotImplementedError

    def registrar_batch(self, operacion, *args, lock=Lock.PESIMISTA, **kwargs):
        batch = Batch(operacion, lock, *args, **kwargs)
        self.batches.append(batch)
        self._publicar_eventos_dominio(batch)

    def _publicar_eventos_dominio(self, batch):
        #for evento in self._obtener_eventos(batches=[batch]):
        #    dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
        pass

    def _publicar_eventos_post_commit(self):
        #for evento in self._obtener_eventos():
        #    dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
        pass

def is_flask():
    try:
        #from flask import session
        return True    
    except Exception as e:
        from fastapi import session        
        return False

def regist_unit_of_work(serialized_obj):
    from app.config.uow import UnitOfWorkSQLAlchemy
    from fastapi import session
    

    session['uow'] = serialized_obj

def flask_uow():
    from fastapi import session
    from app.config.uow import UnitOfWorkSQLAlchemy
    if session.get('uow'):
        return session['uow']
    else:
        uow_serialized = pickle.dumps(UnitOfWorkSQLAlchemy())
        regist_unit_of_work(uow_serialized)
        return uow_serialized

def unit_of_work() -> UnitOfWork:
    if is_flask():
        return pickle.loads(flask_uow())
    else:
        raise Exception('No hay unidad de trabajo')

def save_unit_of_work(uow: UnitOfWork):
    if is_flask():
        regist_unit_of_work(pickle.dumps(uow))
    else:
        raise Exception('No hay unidad de trabajo')


class UnitOfWorkPort:

    @staticmethod
    def commit():
        uow = unit_of_work()
        uow.commit()
        save_unit_of_work(uow)

    @staticmethod
    def rollback(savepoint=None):
        uow = unit_of_work()
        uow.rollback(savepoint=savepoint)
        save_unit_of_work(uow)

    @staticmethod
    def savepoint():
        uow = unit_of_work()
        uow.savepoint()
        save_unit_of_work(uow)

    @staticmethod
    def dar_savepoints():
        uow = unit_of_work()
        return uow.savepoints()

    @staticmethod
    def registrar_batch(operacion, *args, lock=Lock.PESIMISTA, **kwargs):
        uow = unit_of_work()
        uow.registrar_batch(operacion, *args, lock=lock, **kwargs)
        save_unit_of_work(uow)