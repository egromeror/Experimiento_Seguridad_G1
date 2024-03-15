from flask_restful import Resource
from flask import request
import datetime,time
from datetime import date
from ..modelos import db, Evento, EventoSchema

evento_schema = EventoSchema()

class VistaEventosCommands(Resource):
    def post(self):
        print(request.json)
        new_evento = Evento(
            nombre=request.json['nombre'],
            fecha=request.json['fecha'],
            lugar=request.json['lugar']
        )
        db.session.add(new_evento)
        db.session.commit()
        return evento_schema.dump(new_evento)
    
class VistaEventoCommands(Resource):
    def put(self, id):
        evento = Evento.query.get_or_404(id)
        evento.nombre = request.json['nombre']
        evento.fecha = request.json['fecha']
        evento.lugar = request.json['lugar']
        db.session.commit()
        return evento_schema.dump(evento)
    
    def delete(self, id):
        evento = Evento.query.get_or_404(id)
        db.session.delete(evento)
        db.session.commit()
        return '', 204