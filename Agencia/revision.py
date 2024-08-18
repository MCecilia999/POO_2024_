import mysql.connector
from conexion import create_connection, close_connection

class Revision:
    def __init__(self, no_revision, cambiofiltro=None, cambioaceite=None, cambiofrenos=None, otros=None, matricula=None):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otros = otros
        self.matricula = matricula

    @staticmethod
    def create(revision):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO revisiones (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (revision.no_revision, revision.cambiofiltro, revision.cambioaceite, revision.cambiofrenos, revision.otros, revision.matricula))
        connection.commit()
        cursor.close()
        close_connection(connection)

    @staticmethod
    def read(no_revision):
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM revisiones WHERE no_revision = %s"
        cursor.execute(query, (no_revision,))
        result = cursor.fetchone()
        cursor.close()
        close_connection(connection)
        return result

    @staticmethod
    def update(revision):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        UPDATE revisiones 
        SET cambiofiltro = %s, cambioaceite = %s, cambiofrenos = %s, otros = %s, matricula = %s 
        WHERE no_revision = %s
        """
        cursor.execute(query, (revision.cambiofiltro, revision.cambioaceite, revision.cambiofrenos, revision.otros, revision.matricula, revision.no_revision))
        connection.commit()
        cursor.close()
        close_connection(connection)

    @staticmethod
    def delete(no_revision):
        connection = create_connection()
        cursor = connection.cursor()
        query = "DELETE FROM revisiones WHERE no_revision = %s"
        cursor.execute(query, (no_revision,))
        connection.commit()
        cursor.close()
        close_connection(connection)

    @staticmethod
    def see_all():
        connection = create_connection()
        cursor = connection.cursor()
        query = "select * from reviciones"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        close_connection(connection)
