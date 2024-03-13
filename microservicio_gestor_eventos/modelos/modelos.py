from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    lugar = db.Column(db.String(100), nullable=False)

    def __init__(self, nombre, fecha, lugar):
        self.nombre = nombre
        self.fecha = fecha
        self.lugar = lugar

    def __repr__(self):
        return f'<Evento: {self.nombre}>'

class EventoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Evento
        load_instance = True