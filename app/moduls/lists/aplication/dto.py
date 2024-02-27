from dataclasses import dataclass, field
from app.seedwork.aplication.dto import DTO


@dataclass(frozen=True)
class ListDTO(DTO):
    id: str = field(default_factory=str)
    code: str = field(default_factory=str)
    name: str = field(default_factory=str)

@dataclass(frozen=True)
class EstateDTO(DTO):
    id: str = field(default_factory=str)
    code: str = field(default_factory=str)
    name: str = field(default_factory=str) 