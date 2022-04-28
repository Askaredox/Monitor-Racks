import pymysql
import os
from werkzeug.security import generate_password_hash, check_password_hash

class Sql:
    def __init__(self): # TODO: colocar información de base de datos
        self.connection = pymysql.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            passwd=os.environ['DB_PASS'], 
            db=os.environ['DB_DATABASE'], 
            cursorclass=pymysql.cursors.DictCursor, 
            sql_mode=''
        )

    def login(self, correo, contra):
        query = '''
            SELECT * 
            FROM Usuario u
            WHERE correo = %s
        '''
        with self.connection.cursor() as cursor:
            cursor.execute(query, (correo))
            data = cursor.fetchone()
            if(data and check_password_hash(data['contrasena'],contra)):
                return data
            
        return None

    def add_user(self, content):
        contra = generate_password_hash(content['contrasena'])
        query = '''
            INSERT INTO Usuario(nombre, apellido, correo, contrasena, create_time, activar_notif, activar_correo,Tipo_usuario_idTipo_usuario) 
            VALUES(%s,%s,%s,%s,NOW(),0,0,2)
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (content['nombre'], content['apellido'], content['correo'], contra))
                data = cursor.fetchone()
                self.connection.commit()
        except Exception as e:
            return 1, str(e)
        return 0, data

