from flask_restful import Resource, Api
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from datetime import datetime, timedelta, timezone
import simplejson as json
from database import Sql
import os

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ['SECRET_KEY']
cors = CORS(app, resources={r"/*": {"origin": "*"}})
api = Api(app)
jwt = JWTManager(app)
db = Sql()


@api.resource('/')
class Check(Resource):
    def get(self):
        return {'ok': 0, 'mensaje':'todo bien'}, 200


@api.resource('/login')
class Login(Resource):
    def get(self):
        correo = request.args['correo']
        contrasena = request.args['contrasena']
        user = db.login(correo, contrasena)
        if(user != None):
            access_token = create_access_token(identity=user['idUsuario'])
            resp = {'ok': 0, 'access_token': access_token}
            return resp, 200
        else:
            return {'ok': 1, 'mensaje': 'Correo o contraseña no correcto'}, 401

@api.resource('/registro')
class Registro(Resource):
    def post(self):
        content = request.json
        necessary_data = [
            'nombre',
            'apellido',
            'correo',
            'contrasena'
        ]
        if(all(name in content.keys() for name in necessary_data)):
            code, message = db.add_user(content)
            return {'ok': code, 'mensaje':message}, 201 if code == 0 else 403
        return {'ok': 1, 'mensaje':'Data no valida'}, 400


@api.resource('/usuario')
class Usuario(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        code, data = db.get_user_data(current_user)
        return {'ok': code, 'data':data}

    @jwt_required()
    def delete(self):
        current_user = get_jwt_identity()
        code, data = db.delete_user(current_user)
        response = {'ok': code, 'data':data}
        return response

    # def put(self):
    #     content = request.json
    #     necessary_data = [
    #         'carnet',
    #         'nombre'
    #     ]
    #     if(all(name in content.keys() for name in necessary_data)):
    #         return {'ok': True}, 200
    #     else:
    #         return {'status': 1, 'msg':'Data no válida'}, 400



@api.resource('/rack', '/rack/<int:id>')
class Rack(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        code, data = db.get_user_rack(current_user)
        print(data)
        return {'ok': code, 'data':data}, 200

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        content = request.json
        necessary_data = [
            'descripcion'
        ]
        if(all(name in content.keys() for name in necessary_data)):
            code, data = db.add_rack(content, current_user)
            return {'ok': code, 'data':data}, 201
        else:
            return {'status': 1, 'msg':'Data no válida'}, 400

    # def put(self, id):
    #     content = request.json
    #     necessary_data = [
    #         'carnet',
    #         'nombre'
    #     ]
    #     if(all(name in content.keys() for name in necessary_data)):
    #         return {'ok': True}, 200
    #     else:
    #         return {'status': 1, 'msg':'Data no válida'}, 400

    @jwt_required()
    def delete(self, id):
        code, data = db.delete_rack(id)
        response = {'ok': code, 'data':data}
        return response


@api.resource('/batea', '/batea/<int:id>')
class Batea(Resource):
    @jwt_required()
    def get(self, id):
        code, data = db.get_user_batea(id)
        return {'ok': code, 'data':data}, 200

    @jwt_required()
    def post(self):
        content = request.json
        necessary_data = [
            'rack_id',
            'descripcion'
        ]
        if(all(name in content.keys() for name in necessary_data)):
            code, data = db.add_batea(content, content['rack_id'])
            return {'ok': code, 'data':data}, 201
        else:
            return {'status': 1, 'msg':'Data no válida'}, 400

    # def put(self, id):
    #     content = request.json
    #     necessary_data = [
    #         'carnet',
    #         'nombre'
    #     ]
    #     if(all(name in content.keys() for name in necessary_data)):
    #         return {'ok': True}, 200
    #     else:
    #         return {'status': 1, 'msg':'Data no válida'}, 400

    @jwt_required()
    def delete(self, id):
        code, data = db.delete_batea(id)
        response = {'ok': code, 'data':data}
        return response