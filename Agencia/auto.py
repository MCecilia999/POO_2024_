from conexion import create_connection, close_connection

class Auto:
    def __init__(self, matricula, marca=None, modelo=None, color=None, nif=None):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif

    @staticmethod
    def create(auto):
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO autos (matricula, marca, modelo, color, nif) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (auto.matricula, auto.marca, auto.modelo, auto.color, auto.nif))
        connection.commit()
        cursor.close()
        close_connection(connection)

    @staticmethod
    def read(matricula):
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM autos WHERE matricula = %s"
        cursor.execute(query, (matricula,))
        result = cursor.fetchone()
        cursor.close()
        close_connection(connection)
        return result

    @staticmethod
    def verTodo():
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM autos"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        close_connection(connection)
        return result

    @staticmethod
    def update(auto):
        connection = create_connection()
        cursor = connection.cursor()
        query = "UPDATE autos SET marca = %s, modelo = %s, color = %s, nif = %s WHERE matricula = %s"
        cursor.execute(query, (auto.marca, auto.modelo, auto.color, auto.nif, auto.matricula))
        connection.commit()
        cursor.close()
        close_connection(connection)

    @staticmethod
    def delete(matricula):
        connection = create_connection()
        cursor = connection.cursor()
        query = "DELETE FROM autos WHERE matricula = %s"
        cursor.execute(query, (matricula,))
        connection.commit()
        cursor.close()
        close_connection(connection)
    
    @staticmethod
    def see_all():
        connection = create_connection()
        cursor = connection.cursor()
        query = "select * from autos"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        close_connection(connection)


