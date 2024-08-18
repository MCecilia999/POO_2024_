import mysql.connector
from conexionDB import conexion

class Nota:
    def __init__(self, usuario_id, titulo, descripcion, fecha):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha

    @staticmethod
    def crear_nota(nota):
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO notas (usuario_id, titulo, descripcion, fecha) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nota.usuario_id, nota.titulo, nota.descripcion, nota.fecha))
            conexion.commit()
            print("Nota creada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

    @staticmethod
    def obtener_nota(id):
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT * FROM notas WHERE id = %s"
            cursor.execute(sql, (id,))
            nota = cursor.fetchone()
            return nota
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

    @staticmethod
    def actualizar_nota(id, nota):
        try:
            cursor = conexion.cursor()
            sql = """
            UPDATE notas SET usuario_id = %s, titulo = %s, descripcion = %s, fecha = %s 
            WHERE id = %s
            """
            cursor.execute(sql, (nota.usuario_id, nota.titulo, nota.descripcion, nota.fecha, id))
            conexion.commit()
            print("Nota actualizada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

    @staticmethod
    def eliminar_nota(id):
        try:
            cursor = conexion.cursor()
            sql = "DELETE FROM notas WHERE id = %s"
            cursor.execute(sql, (id,))
            conexion.commit()
            print("Nota eliminada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
