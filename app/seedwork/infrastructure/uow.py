from abc import ABC, abstractmethod
from enum import Enum
from click import UUID

from app.seedwork.domain.entities import RootAggregation
from pydispatch import dispatcher

import pickle


class Lock(Enum):
    OPTIMISTA = 1
    PESIMISTA = 2

class Batch:
    def __init__(self, operation, lock: Lock = Lock.PESIMISTA, *args, **kwargs):
        self.operation = operation
        self.args = args
        self.lock = lock
        self.kwargs = kwargs

class UnitOfWork(ABC):

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def _get_events(self, batches=None):
        batches = self.batches if batches is None else batches
        for batch in batches:
            for arg in batch.args:
                if isinstance(arg, RootAggregation):
                    return arg.events
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
        self._publish_events_post_commit()
        self._limpiar_batches()

    @abstractmethod
    def rollback(self, savepoint=None):
        self._limpiar_batches()
    
    @abstractmethod
    def savepoint(self):
        raise NotImplementedError

    def regist_batch(self, operation, *args, lock, **kwargs):
        batch = Batch(operation, lock, *args, **kwargs)
        self.batches.append(batch)
        self._publish_domain_events(batch)

    def _publish_domain_events(self, batch):
        for event in self._get_events(batches=[batch]):
            print('event: ', event)
            dispatcher.send(signal=f'{type(event).__name__}Domain', evento=event)
        pass

    def _publish_events_post_commit(self):
        for event in self._get_events():           
            dispatcher.send(signal=f'{type(event).__name__}Integracion', evento=event)
        pass

def is_flask():
    try:
        from flask import session
        return True    
    except Exception as e:
        return False

def regist_unit_of_work(serialized_obj):
    from app.config.uow import unitOfWorkSQLAlchemy
    from flask import session
    session['uow'] = serialized_obj

def flask_uow():
    from flask import session
    from app.config.uow import unitOfWorkSQLAlchemy
    if session.get('uow'):
       return session['uow']
    else:
       uow_serialized = pickle.dumps(unitOfWorkSQLAlchemy())
       regist_unit_of_work(uow_serialized)
       return uow_serialized


def unit_of_work() -> UnitOfWork:
    if is_flask():
        return pickle.loads(flask_uow())
    else:
        raise Exception('No hay unidad de trabajo')

def save_unit_of_work(uow: UnitOfWork):
    regist_unit_of_work(pickle.dumps(uow))
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
    def regist_batch(operation, *args, lock=Lock.OPTIMISTA, **kwargs):
        uow = unit_of_work()
        uow.regist_batch(operation, *args, lock=lock, **kwargs)
        save_unit_of_work(uow)