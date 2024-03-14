import redis
from flask import Flask
import threading
import json
import requests

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
    return 'Hola, soy el microservicio 1'

urlApi = "http://127.0.0.1:5001/eventos"
def actuar(new_evento):
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(new_evento)
    print(json_data)
    conn = requests.post(urlApi, data=json_data, headers=headers)
    response = conn.text
    return response

# Encargado de recibir request del Api Gateway
def get_request_gestor_eventos():
    servicioEscuchaEventos = r.pubsub()
    servicioEscuchaEventos.subscribe('Eventos')
    try:
        for message in servicioEscuchaEventos.listen():
            try:
                try:
                    message_data = json.loads(message['data'])
                except:
                    continue
                
                print(f"Evento recibido: {message_data}")
                r.publish("EventosVerificados", json.dumps(message_data))
            except json.JSONDecodeError:
                print(f"Error: {message['data']}")
            except KeyError:
                print(f"Error: {message['data']}")
    except (redis.exceptions.ConnectionError, redis.exceptions.TimeoutError) as e:
        print(f"Error de conexión: {e}")

def send_request_gestor():
    servicioEscuchaEventosVerificados = r.pubsub()
    servicioEscuchaEventosVerificados.subscribe('EventosVerificados')

    try:
        for message in servicioEscuchaEventosVerificados.listen():
            try:
                try:
                    message_data = json.loads(message['data'])
                except:
                    continue
                
                status_code = actuar(json.dumps(message_data))
                print(status_code)
                print(f"Evento verificado: {message_data}")
            except json.JSONDecodeError:
                print(f"Error: {message['data']}")
            except KeyError:
                print(f"Error: {message['data']}")
    except (redis.exceptions.ConnectionError, redis.exceptions.TimeoutError) as e:
        print(f"Error de conexión: {e}")


t1 = threading.Thread(target=get_request_gestor_eventos)
t2 = threading.Thread(target=send_request_gestor)
t1.start()
t2.start()
#while True:
    