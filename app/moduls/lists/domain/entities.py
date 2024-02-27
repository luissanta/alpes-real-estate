"""Entidades del dominio de lists

En este archivo usted encontrará las entidades del dominio de lists
"""

from __future__ import annotations
from dataclasses import dataclass, field
import app.moduls.lists.domain.value_objects as ov
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class Estate(Entity):
    id: int = field(default=None)
    code: str = field(default_factory=str)
    name: str = field(default_factory=str)

@dataclass
class List(RootAggregation):
    estate_id: int = field(hash=True, default=None)
    estates: list[Estate] = field(default_factory=list)
