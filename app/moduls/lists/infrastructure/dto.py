"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos
"""

from app.config.db import Base, engine
from sqlalchemy import Column, String


class Estate(Base):
    __tablename__ = "estatelist"
    id = Column(String, primary_key=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)
