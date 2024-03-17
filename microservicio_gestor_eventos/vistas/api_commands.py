from flask_restful import Resource
from flask import request
import datetime,time
from datetime import date
from ..modelos import db, Evento, EventoSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

evento_schema = EventoSchema()

class VistaEventosCommands(Resource):

    @jwt_required()
    def post(self):
        identity = get_jwt_identity()

        if identity == 'UsrEvento':
            new_evento = Evento(
                nombre=request.json['nombre'],
                fecha=request.json['fecha'],
                lugar=request.json['lugar']
            )
            db.session.add(new_evento)
            db.session.commit()
            return evento_schema.dump(new_evento)
        else:
            return {'mensaje': 'Usuario no autorizado'}, 401

        
class VistaEventoCommands(Resource):

    @jwt_required()
    def put(self, id):
        identity = get_jwt_identity()

        if identity == 'UsrEvento':
            evento = Evento.query.get_or_404(id)
            evento.nombre = request.json['nombre']
            evento.fecha = request.json['fecha']
            evento.lugar = request.json['lugar']
            db.session.commit()
            return evento_schema.dump(evento)
        else:
            return {'mensaje': 'Usuario no autorizado'}, 401

        
    
    @jwt_required()
    def delete(self, id):
        identity = get_jwt_identity()

        if identity == 'UsrEvento':
            evento = Evento.query.get_or_404(id)
            db.session.delete(evento)
            db.session.commit()
            return '', 204
        else:
            return {'mensaje': 'Usuario no autorizado'}, 401            

        