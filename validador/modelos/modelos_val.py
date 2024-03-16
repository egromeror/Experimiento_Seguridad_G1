from flask_sqlalchemy import SQLAlchemy 
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import hashlib

db = SQLAlchemy()

class Evento_valid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    fecha = db.Column(db.DateTime)
    lugar = db.Column(db.String(50))
    hash = db.Column(db.String(64))  

    def generate_hash(self):
        # Se genera un hash a partir de la info del evento
        hash_obj = hashlib.sha256()
        hash_obj.update(self.nombre.encode('utf-8'))
        hash_obj.update(self.fecha.isoformat().encode('utf-8'))
        hash_obj.update(self.lugar.encode('utf-8'))
        self.hash = hash_obj.hexdigest()


class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    fecha = db.Column(db.DateTime)
    lugar = db.Column(db.String(50))

class EventoSchema_valid(SQLAlchemyAutoSchema):
    class Meta:
        model = Evento_valid
        load_instance = True


