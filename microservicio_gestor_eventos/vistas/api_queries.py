from flask_restful import Resource
from flask import request
from datetime import datetime, timedelta 
from ..modelos import db, Evento, EventoSchema

evento_schema = EventoSchema()

class VistaEventosQueries(Resource):
    def get(self):
        return [evento_schema.dump(evento) for evento in Evento.query.all()]
    
class VistaEventoQueries(Resource):
    def get(self, id):
        evento = Evento.query.get(id)
        return evento_schema.dump(evento)