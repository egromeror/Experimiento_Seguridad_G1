from flask_restful import Resource
from flask import request
import datetime,time
from datetime import date
from ..modelos import db, Evento, EventoSchema

evento_schema = EventoSchema()

class VistaEventosCommands(Resource):
    def post(self):
        new_evento = Evento(
            nombre=request.json['nombre'],
            fecha=datetime.datetime.strptime(request.json['fecha'],'%d/%m/%Y'),
            lugar=request.json['lugar']
        )
        db.session.add(new_evento)
        db.session.commit()
        return evento_schema.dump(new_evento)
    
class VistaEventoCommands(Resource):
    def put(self, id):
        evento = Evento.query.get_or_404(id)
        evento.nombre = request.json['nombre']
        pfecha = datetime.datetime.strptime(request.json['fecha'],'%d/%m/%Y')
        pfecha2 = pfecha.strftime("%d/%m/%Y, %H:%M:%S")
        print(pfecha)
        print(pfecha2)
        # evento.fecha = datetime.datetime.utcnow(),
        evento.lugar = request.json['lugar']
        db.session.commit()
        return evento_schema.dump(evento)
    
    def delete(self, id):
        evento = Evento.query.get_or_404(id)
        db.session.delete(evento)
        db.session.commit()
        return '', 204