import pymysql
import os
from werkzeug.security import generate_password_hash, check_password_hash

class Sql:
    def __init__(self): 
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
                
                self.connection.commit()
        except Exception as e:
            return 1, str(e)
        return 0, 'Usuario registrado correctamente'

    def get_user_data(self, user_id):
        query = '''
            SELECT nombre, apellido, correo, activar_notif, activar_correo from Usuario u 
            WHERE idUsuario = %s
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (user_id))
                data = cursor.fetchone()
        except Exception as e:
            return 1, str(e)
        return 0, data

    def delete_user(self, user_id):
        query = '''
            DELETE FROM Usuario u 
            WHERE u.idUsuario = %s
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (user_id))
                self.connection.commit()
        except Exception as e:
            return 1, str(e)
        return 0, 'Usuario eliminado correctamente'

    def get_user_rack(self, user_id):
        query = '''
            SELECT * from Rack
            WHERE Usuario_idUsuario = %s
        '''
        query_batea = '''
            SELECT * from Batea
            WHERE Rack_idRack = %s
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (user_id))
                data = cursor.fetchall()
                if(data is not None):
                    for d in data:
                        cursor.execute(query_batea, (d['idRack']))
                        bateas = cursor.fetchall()
                        d['bateas'] = bateas if bateas else []

        except Exception as e:
            return 1, str(e)
        return 0, data
    
    def add_rack(self, content, user_id):
        query = '''
            INSERT INTO Rack(descripcion, Usuario_idUsuario) 
            VALUES(%s,%s)
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (content['descripcion'], user_id))
                
                self.connection.commit()
        except Exception as e:
            return 1, str(e)
        return 0, 'Rack agregado correctamente'

    def delete_rack(self, id_rack):
        query = '''
            DELETE FROM Rack
            WHERE idRack = %s
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (id_rack))
                self.connection.commit()
        except Exception as e:
            return 1, str(e)
        return 0, 'Rack eliminado correctamente'

    def get_user_batea(self, batea_id):
        query = '''
            SELECT * from Batea
            WHERE idBatea = %s
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (batea_id))
                data = cursor.fetchone()

        except Exception as e:
            return 1, str(e)
        return 0, data

    def add_batea(self, content, rack_id):
        query = '''
            INSERT INTO Batea(descripcion, temperatura, encendido, Rack_idRack) 
            VALUES(%s,%s,%s,%s)
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (content['descripcion'], 0.00, False, rack_id))
                
                self.connection.commit()
        except Exception as e:
            return 1, str(e)
        return 0, 'Batea agregado correctamente'

    def delete_batea(self, batea_id):
        query = '''
            DELETE FROM Batea
            WHERE idBatea = %s
        '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (batea_id))
                self.connection.commit()
        except Exception as e:
            return 1, str(e)
        return 0, 'Batea eliminado correctamente'
        