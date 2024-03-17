from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token


class VistaToken(Resource):

    
    def post(self):
        usuariosLista = ["UsrTest", "UsrEvento", "UsrToken"]

        usuario = request.json["user"]
        clave = request.json["password"]    

        if usuario in usuariosLista and clave == "123456": 
            access_token = create_access_token(identity=usuario)
            return {"mensaje": "Usuario autorizado", "token":access_token}
        else:
            return "Verifique los datos ingresados", 401                        
        
        
        