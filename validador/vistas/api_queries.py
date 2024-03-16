from flask_restful import Resource
from flask import request
import datetime,time
from datetime import date
from ..modelos.modelos_val import Evento_valid, EventoSchema_valid

evento_schema = EventoSchema_valid()

class VistaValid_EventosQueries(Resource):
    def get(self):
        return [evento_schema.dump(evento) for evento in Evento_valid.query.all()]
    
class VistaValid_EventoQueries(Resource):
    def get(self, id):
        evento = Evento_valid.query.get(id)
        return evento_schema.dump(evento)