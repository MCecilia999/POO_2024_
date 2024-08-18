import mysql.connector
from conexion import create_connection, close_connection

class Cliente:
    def __init__(self, nif, nombre=None, direccion=None, ciudad=None, telefono=None):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono

    @staticmethod
    def create(cliente):
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO clientes (nif, nombre, direccion, ciudad, telefono) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (cliente.nif, cliente.nombre, cliente.direccion, cliente.ciudad, cliente.telefono))
        connection.commit()
        cursor.close()
        close_connection(connection)

    @staticmethod
    def read(nif):
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM clientes WHERE nif = %s"
        cursor.execute(query, (nif,))
        result = cursor.fetchone()
        cursor.close()
        close_connection(connection)
        return result

    @staticmethod
    def update(cliente):
        connection = create_connection()
        cursor = connection.cursor()
        query = "UPDATE clientes SET nombre = %s, direccion = %s, ciudad = %s, telefono = %s WHERE nif = %s"
        cursor.execute(query, (cliente.nombre, cliente.direccion, cliente.ciudad, cliente.telefono, cliente.nif))
        connection.commit()
        cursor.close()
        close_connection(connection)

    @staticmethod
    def delete(nif):
        connection = create_connection()
        cursor = connection.cursor()
        query = "DELETE FROM clientes WHERE nif = %s"
        cursor.execute(query, (nif,))
        connection.commit()
        cursor.close()
        close_connection(connection)
    
    @staticmethod
    def see_all():
        connection = create_connection()
        cursor = connection.cursor()
        query = "select * from clientes"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        close_connection(connection)

    
