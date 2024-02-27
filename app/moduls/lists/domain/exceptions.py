""" Excepciones del dominio de vuelos

En este archivo usted encontrará los Excepciones relacionadas al dominio de lists
"""

from app.seedwork.domain.exceptions import FactoryException


class ObjectTypeNotExistInEstatesDomainException(FactoryException):
    def __init__(self, message='No existe una fábrica para el tipo solicitado en el módulo de propiedades'):
        self.__message = message

    def __str__(self):
        return str(self.__message)
