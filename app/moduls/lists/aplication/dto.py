from dataclasses import dataclass, field
from app.seedwork.aplication.dto import DTO

@dataclass(frozen=True)
class CompaniesDTO(DTO):
    company_name: str = field(default_factory=str)
    location: str = field(default_factory=str)
    typeCompany: str = field(default_factory=str)

@dataclass(frozen=True)
class GeoLocationDTO(DTO):
    #id: str = field(default_factory=str)
    lat: str = field(default_factory=str)
    lon: str = field(default_factory=str) 

@dataclass(frozen=True)
class EstateDTO(DTO):
    #id: str = field(default_factory=str)
    code: str = field(default_factory=str)
    name: str = field(default_factory=str) 
    geo_locations: list[GeoLocationDTO] = field(default_factory=list[GeoLocationDTO])
    companies: list[CompaniesDTO] = field(default_factory=list[CompaniesDTO])


@dataclass(frozen=True)
class ListDTO(DTO):
    id: str = field(default_factory=str)
    estates: list[EstateDTO] = field(default_factory=list[EstateDTO])