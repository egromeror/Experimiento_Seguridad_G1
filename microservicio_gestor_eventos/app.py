from microservicio_gestor_eventos import create_app
from flask_restful import Api
from flask_cors import CORS
from .modelos import db
from .vistas import VistaEventosCommands,VistaEventoCommands,VistaEventosQueries,VistaEventoQueries

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)

api.add_resource(VistaEventosCommands, '/eventos')
api.add_resource(VistaEventoCommands, '/evento/<int:id>')
api.add_resource(VistaEventosQueries, '/eventos')
api.add_resource(VistaEventoQueries, '/evento/<int:id>')

@app.route('/')
def hello():
    return 'Hola, soy el microservicio 1'
