from dataclasses import dataclass, field
from app.seedwork.aplication.dto import DTO


@dataclass(frozen=True)
class ListDTO(DTO):
    id: int = field(default_factory=int)
    code: str = field(default_factory=str)
    name: str = field(default_factory=str)

@dataclass(frozen=True)
class EstateDTO(DTO):
    id: int = field(default_factory=int)
    code: str = field(default_factory=str)
    name: str = field(default_factory=str) 


@dataclass(frozen=True)
class ListDTO(DTO):
    estates: list[EstateDTO] = field(default_factory=list)