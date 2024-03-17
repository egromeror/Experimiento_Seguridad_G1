from flask import Flask, jsonify
from flask_jwt_extended import JWTManager


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventos_deportivos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "secret-jwt"
    app.config["PROPAGATE_EXCEPTIONS"] = True

    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"mensaje": "Token ha expirado", "error": "token expirado"}),401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"mensaje": "Error al validar el token", "error": "token invalido"}),401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {"mensaje": "Request no contiene un token","error": "token requerido"}),401,
        )
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        
        if identity == "UsrTest2":
            print("entro: " + identity )
            return identity
        else:
            return (
            jsonify(
                {"mensaje": "Usuario no autorizado","error": "token invalido"}),401,)


    return app