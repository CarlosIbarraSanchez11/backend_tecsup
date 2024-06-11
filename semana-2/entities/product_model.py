"""
id
name
description
price
stock
created_at
updated_at

tablename = products
"""
from extensions import db
from datetime import datetime, timezone
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    # PARA PODEMOS MOSTRAR LA INFORMACION DE LA TABLA USER EN LA RESPUESTA DE
    # MI API, DEBEMOS PARSEAR ESTA INFORMACIÓN
    # to_dict => Conviertirlo a un diccionario de datos (objeto)
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

