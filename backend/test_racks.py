from unittest import TestCase, main as unittest_main
import requests
import simplejson as json

class TestEstudiante(TestCase):
    URL = 'http://192.168.1.5:5000'
    token = ''
    rack = ''

    def test_01_check(self):
        r = requests.get(self.URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['ok'], 0)

    def test_02_registro(self):
        data = {
            "nombre":"Dummy",
            "apellido":"Doe",
            "correo":"qwerty@gmail.com",
            "contrasena":"Test1234"
        }
        
        r = requests.post(self.URL+'/registro', json=data)
        # self.assertEqual(r.status_code, 201)
        self.assertDictEqual({'ok': 0, 'mensaje':'Usuario registrado correctamente'},r.json())

    def test_03_login(self):
        r = requests.get(self.URL+'/login?correo=qwerty@gmail.com&contrasena=Test1234')
        response = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(response['ok'],0)
        self.__class__.token = response['access_token']
        self.assertTrue(type(self.token) is str)

    def test_04_usuario(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.__class__.token)
        }
        r = requests.get(self.URL+'/usuario', headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({'ok': 0,'data':{
            "nombre":"Dummy",
            "apellido":"Doe",
            "correo":"qwerty@gmail.com",
            "activar_notif":0, 
            "activar_correo":0
        }},r.json())

    def test_05_add_rack(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.__class__.token)
        }
        data = {
            "descripcion":"Rack prueba"
        }
        r = requests.post(self.URL+'/rack', headers=headers, json=data)
        self.assertEqual(r.status_code, 201)
        self.assertDictEqual(r.json(), {'ok': 0, 'data': 'Rack agregado correctamente'})

    def test_06_get_rack(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.__class__.token)
        }
        r = requests.get(self.URL+'/rack', headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['ok'], 0)
        self.__class__.rack = r.json()['data'][0]['idRack']

    def test_07_add_batea(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.__class__.token)
        }
        data = {
            "rack_id": self.__class__.rack,
            "descripcion":"Batea de prueba"
        }
        r = requests.post(self.URL+'/batea', headers=headers, json=data)
        self.assertEqual(r.status_code, 201)
        self.assertDictEqual(r.json(), {'ok': 0, 'data': 'Batea agregado correctamente'})

    def test_10_delete_usuario(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.__class__.token)
        }
        r = requests.delete(self.URL+'/usuario', headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({'ok': 0,'data':'Usuario eliminado correctamente'},r.json())

if __name__ == '__main__':
    unittest_main()