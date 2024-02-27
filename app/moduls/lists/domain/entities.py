"""Entidades del dominio de lists

En este archivo usted encontrará las entidades del dominio de vuelos
"""

from __future__ import annotations
from dataclasses import dataclass, field
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class Estate(Entity):
    id: int = field(default=None)
    code: str = field(default_factory=str)
    name: str = field(default_factory=str)


@dataclass
class EstateList(RootAggregation):
    estate_id: int = field(hash=True, default=None)
    estates: list[Estate] = field(default_factory=list)

    
  

