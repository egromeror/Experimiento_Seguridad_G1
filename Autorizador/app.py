from Autorizador import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .vistas import VistaToken 


app = create_app('default')
app_context = app.app_context()
app_context.push()

app.config["JWT_SECRET_KEY"] = "secret-jwt"  # Change this!
jwt = JWTManager(app)
api = Api(app)

api.add_resource(VistaToken, '/token')

@app.route('/')
def hello():
    return 'Hola, soy autorizador'