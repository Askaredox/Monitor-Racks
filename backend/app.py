from flask_restful import Resource, Api
from flask import Flask, request
from flask_cors import CORS
import simplejson as json


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})
api = Api(app)



@api.resource('/')
class Check(Resource):
    def get(self):
        return {'ok': True}


@api.resource('/login')
class Login(Resource):
    def get(self):
        return {'ok': True}


@api.resource('/usuario', '/usuario/<int:id>')
class Usuario(Resource):
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)