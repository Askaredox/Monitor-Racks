import unittest
import requests
import simplejson as json

class TestEstudiante(unittest.TestCase):
    URL = 'http://172.19.0.3:3000'
    id_e = 12
    def test_01_check(self):
        r = requests.get(self.URL)
        self.assertEqual(r.status_code, 200)
        self.assertTrue(r.json()['ok'])
