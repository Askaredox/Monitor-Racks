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
            return {'ok': 0, 'access_token': access_token}, 200
        else:
            return {'ok': 1, 'mensaje': 'Correo o contraseña no correcto'}, 401

@api.resource('/logout')
class Logout(Resource):
    def get(self):
        unset_jwt_cookies('Logout correcto')
        return {'ok': 1, 'mensaje': 'Logout correcto'}, 200
            

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
            return {'ok': code, 'mensaje':message}, 200 if code == 0 else 403
        return {'ok': 1, 'mensaje':'Data no valida'}, 400


@api.resource('/usuario', '/usuario/<int:id>')
class Usuario(Resource):
    def get(self, id):
        return {'ok': True}

    def put(self, id):
        content = request.json
        necessary_data = [
            'carnet',
            'nombre'
        ]
        if(all(name in content.keys() for name in necessary_data)):
            return {'ok': True}, 200
        else:
            return {'status': 1, 'msg':'Data no válida'}, 400


@api.resource('/rack', '/rack/<int:id>')
class Rack(Resource):
    def get(self, id):
        return {'ok': True}

    def post(self):
        content = request.json
        necessary_data = [
            'carnet',
            'nombre'
        ]
        if(all(name in content.keys() for name in necessary_data)):
            return {'ok': True}, 200
        else:
            return {'status': 1, 'msg':'Data no válida'}, 400

    def put(self, id):
        content = request.json
        necessary_data = [
            'carnet',
            'nombre'
        ]
        if(all(name in content.keys() for name in necessary_data)):
            return {'ok': True}, 200
        else:
            return {'status': 1, 'msg':'Data no válida'}, 400

    def delete(self, id):
        return {'ok': True}


@api.resource('/batea', '/batea/<int:id>')
class Batea(Resource):
    def get(self, id):
        return {'ok': True}

    def post(self):
        content = request.json
        necessary_data = [
            'carnet',
            'nombre'
        ]
        if(all(name in content.keys() for name in necessary_data)):
            return {'ok': True}, 200
        else:
            return {'status': 1, 'msg':'Data no válida'}, 400

    def put(self, id):
        content = request.json
        necessary_data = [
            'carnet',
            'nombre'
        ]
        if(all(name in content.keys() for name in necessary_data)):
            return {'ok': True}, 200
        else:
            return {'status': 1, 'msg':'Data no válida'}, 400

    def delete(self, id):
        return {'ok': True}


@api.resource('/historial', '/historial/<int:id>')
class Historial(Resource):
    def get(self):
        return {'ok': True}

    def post(self):
        content = request.json
        necessary_data = [
            'carnet',
            'nombre'
        ]
        if(all(name in content.keys() for name in necessary_data)):
            return {'ok': True}, 200
        else:
            return {'status': 1, 'msg':'Data no válida'}, 400

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)