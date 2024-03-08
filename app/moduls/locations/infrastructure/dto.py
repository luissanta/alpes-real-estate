"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos
"""

from app.config.db import db
from sqlalchemy import Column, String

Base = db.declarative_base()

list_locations_location = db.Table(
    "list_locations_locations",
    db.Model.metadata,
    db.Column("id", db.String, db.ForeignKey("list_locations.id")),
    db.Column("location_id", db.String),
    db.Column("code", db.String),
    db.Column("name", db.String),
    db.Column("uniquecode", db.String),
    db.ForeignKeyConstraint(
        ["location_id", "uniquecode"],
        ["location.location_id", "location.uniquecode"]
    )
)

class Location(db.Model):
    __tablename__ = "location"
    location_id = db.Column(db.String, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    uniquecode = db.Column(db.String, primary_key=True)

class List_locations(db.Model):
    __tablename__ = "list_locations"
    id = db.Column(db.String, primary_key=True)    
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
    locations = db.relationship('Location', secondary=list_locations_location, backref='list_locations')    