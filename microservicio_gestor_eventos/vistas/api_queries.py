from flask_restful import Resource
from ..modelos import db, Evento, EventoSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify

evento_schema = EventoSchema()

class VistaEventosQueries(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        
        if identity == 'UsrEvento':
            return [evento_schema.dump(evento) for evento in Evento.query.all()]
        else:
            return {'mensaje': 'Usuario no autorizado'}, 401
        
        
    
class VistaEventoQueries(Resource):
    @jwt_required()
    def get(self, id):
        identity = get_jwt_identity()

        if identity == 'UsrEvento':
            evento = Evento.query.get(id)
            return evento_schema.dump(evento)
        else:
            return {'mensaje': 'Usuario no autorizado'}, 401

        