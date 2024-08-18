import mysql.connector
from conexionDB import conexion
from conexionDB import *
import hashlib
import datetime

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def crear_usuario(usuario):
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO usuarios (nombre, apellidos, email, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (usuario.nombre, usuario.apellidos, usuario.email, usuario.password))
            conexion.commit()
            print("Usuario creado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

    @staticmethod
    def obtener_usuario(id):
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT * FROM usuarios WHERE id = %s"
            cursor.execute(sql, (id,))
            usuario = cursor.fetchone()
            return usuario
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
    
    @staticmethod
    def obtener_usuario_por_email(email):
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(sql, (email,))
            usuario = cursor.fetchone()
            return usuario
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

    @staticmethod
    def actualizar_usuario(id, usuario):
        try:
            cursor = conexion.cursor()
            sql = """
            UPDATE usuarios SET nombre = %s, apellidos = %s, email = %s, password = %s, fecha = %s 
            WHERE id = %s
            """
            cursor.execute(sql, (usuario.nombre, usuario.apellidos, usuario.email, usuario.password, usuario.fecha, id))
            conexion.commit()
            print("Usuario actualizado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

    @staticmethod
    def eliminar_usuario(id):
        try:
            cursor = conexion.cursor()
            sql = "DELETE FROM usuarios WHERE id = %s"
            cursor.execute(sql, (id,))
            conexion.commit()
            print("Usuario eliminado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
