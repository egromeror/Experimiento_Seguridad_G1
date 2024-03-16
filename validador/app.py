import redis
from flask import Flask
import datetime
import json
import time

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    decode_responses=True
)

@app.route('/')
def hello():
    return 'Hola, soy el api gateway'

class Evento:
   def __init__(self, nombre, fecha, lugar):
    self.nombre = nombre
    self.fecha = fecha
    self.lugar = lugar

def serialize_datetime(obj): 
    if isinstance(obj, datetime.datetime): 
        return obj.isoformat() 
    raise TypeError("Type not serializable") 

while True:
   time.sleep(10)   
   new_evento = Evento(
       nombre="Evento 1",
       fecha=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
       lugar="Lugar 1"
   )
   
   eventoJSONData = json.dumps(new_evento.__dict__,indent=2, default=serialize_datetime)
   print(eventoJSONData)
   r.publish("Eventos", eventoJSONData)   