from flask_restful import Resource
from flask import request
import datetime,time
from datetime import date
from validador.modelos.modelos_val import db, Evento_valid, EventoSchema_valid

evento_schema = EventoSchema_valid()

class VistaValid_EventosCommands(Resource):
    def post(self):
        print(request.json)
        new_evento = Evento_valid(
            nombre=request.json['nombre'],
            fecha=request.json['fecha'],
            lugar=request.json['lugar'],
            hash = request.json['hash']
        )
        db.session.add(new_evento)
        db.session.commit()
        return evento_schema.dump(new_evento)
    
class VistaValid_EventoCommands(Resource):
    def put(self, id):
        evento = Evento_valid.query.get_or_404(id)
        evento.nombre = request.json['nombre']
        evento.fecha = request.json['fecha']
        evento.lugar = request.json['lugar']
        evento.hash = request.json['hash']
        db.session.commit()
        return evento_schema.dump(evento)
    
    def delete(self, id):
        evento = Evento_valid.query.get_or_404(id)
        db.session.delete(evento)
        db.session.commit()
        return '', 204
