"""Entidades reusables parte del seedwork del proyecto

En este archivo usted encontrará las entidades reusables parte del seedwork del proyecto
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from app.seedwork.domain.events import DomainEvent


@dataclass
class Entity:
    id: int = field(hash=True)
    created_at: datetime = field(default=datetime.now())
    updated_at: datetime = field(default=datetime.now())
        

@dataclass
class RootAggregation(Entity):
    events: List[DomainEvent] = field(default_factory=list)

    def add_events(self, event: DomainEvent):
        self.events.append(event)
    
    def clear_events(self):
        self.events = list()
