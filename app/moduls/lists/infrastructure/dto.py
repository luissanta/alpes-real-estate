"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos
"""

from app.config.db import db
from sqlalchemy import Column, String

Base = db.declarative_base()

list_estates_estate = db.Table(
    "list_estates_estates",
    db.Model.metadata,
    db.Column("id", db.String, db.ForeignKey("list_estates.id")),
    db.Column("estate_id", db.String),
    db.Column("code", db.String),
    db.Column("name", db.Integer),
    db.ForeignKeyConstraint(
        ["estate_id", "code", "name"],
        ["estate.estate_id", "estate.code", "estate.name"]
    )
)

class Estate(db.Model):
    __tablename__ = "estate"
    estate_id = db.Column(db.String, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

class List_estates(db.Model):
    __tablename__ = "list_estates"
    id = db.Column(db.String, primary_key=True)    
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
    estates = db.relationship('Estate', secondary=list_estates_estate, backref='list_estates')    