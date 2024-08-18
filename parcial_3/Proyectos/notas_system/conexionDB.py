import mysql.connector

try:
    #Conectar con la BD MySQL
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_notas'
)
except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un problema con el servidor  porfavor intentelo mas tarde")

#verificar la conexion a la BD
else:
    print(f"Se creo la conexion con la BD exitosamente")