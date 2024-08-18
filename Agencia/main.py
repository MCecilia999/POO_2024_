from auto import Auto
from cliente import Cliente
from revision import Revision

def mostrar_menu_principal():
    print("===== Menú Principal =====")
    print("1. Gestionar Autos")
    print("2. Gestionar Clientes")
    print("3. Gestionar Revisiones")
    print("4. Salir")
    print("==========================")

def mostrar_menu_autos():
    print("===== Menú de Gestión de Autos =====")
    print("1. Crear Auto")
    print("2. Leer Auto")
    print("3. Actualizar Auto")
    print("4. Eliminar Auto")
    print("5. Ver todos los Autos")
    print("6. Volver al Menú Principal")
    print("===================================")

def mostrar_menu_clientes():
    print("===== Menú de Gestión de Clientes =====")
    print("1. Registrar Cliente")
    print("2. Leer Cliente")
    print("3. Volver al Menú Principal")
    print("=======================================")

def mostrar_menu_revisiones():
    print("===== Menú de Gestión de Revisiones =====")
    print("1. Crear Revisión")
    print("2. Leer Revisión")
    print("3. Actualizar Revisión")
    print("4. Eliminar Revisión")
    print("5. Ver todas las Revisiones")
    print("6. Volver al Menú Principal")
    print("========================================")

def crear_auto():
    matricula = input("Ingrese la matrícula del auto: ")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    color = input("Ingrese el color del auto: ")
    nif = input("Ingrese el NIF del cliente asociado: ")
    auto = Auto(matricula, marca, modelo, color, nif)
    Auto.create(auto)
    print("Auto creado exitosamente.")

def buscar_auto():
    matricula = input("Ingrese la matrícula del auto a buscar: ")
    auto = Auto.read(matricula)
    if auto:
        print(f"Matricula: {auto['matricula']}")
        print(f"Marca: {auto['marca']}")
        print(f"Modelo: {auto['modelo']}")
        print(f"Color: {auto['color']}")
        print(f"NIF del Cliente: {auto['nif']}")
    else:
        print("Auto no encontrado.")

def ver_autos():
    autos = Auto.verTodo()
    if autos:
        for auto in autos:
            print(f"--Auto--")
            print(f"Matricula: {auto['matricula']}")
            print(f"Marca: {auto['marca']}")
            print(f"Modelo: {auto['modelo']}")
            print(f"Color: {auto['color']}")
            print(f"NIF del Cliente: {auto['nif']}")
    else:
        print("No se encontraron autos.")

def actualizar_auto():
    matricula = input("Ingrese la matrícula del auto a actualizar: ")
    auto_existente = Auto.read(matricula)
    if auto_existente:
        marca = input(f"Nuevo valor para marca (actual: {auto_existente['marca']}): ")
        modelo = input(f"Nuevo valor para modelo (actual: {auto_existente['modelo']}): ")
        color = input(f"Nuevo valor para color (actual: {auto_existente['color']}): ")
        nif = input(f"Nuevo valor para NIF del cliente (actual: {auto_existente['nif']}): ")
        auto = Auto(matricula, marca if marca else auto_existente['marca'],
                           modelo if modelo else auto_existente['modelo'],
                           color if color else auto_existente['color'],
                           nif if nif else auto_existente['nif'])
        Auto.update(auto)
        print("Auto actualizado exitosamente.")
    else:
        print("Auto no encontrado.")

def eliminar_auto():
    matricula = input("Ingrese la matrícula del auto a eliminar: ")
    Auto.delete(matricula)
    print("Auto eliminado exitosamente.")

def registrar_cliente():
    nif = input("Ingrese el NIF del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    ciudad = input("Ingrese la ciudad del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    cliente = Cliente(nif, nombre, direccion, ciudad, telefono)
    Cliente.create(cliente)
    print("Cliente registrado exitosamente.")

def ver_cliente():
    nif = input("Ingrese el NIF del cliente a buscar: ")
    cliente = Cliente.read(nif)
    if cliente:
        print(f"NIF: {cliente['nif']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"Ciudad: {cliente['ciudad']}")
        print(f"Teléfono: {cliente['telefono']}")
    else:
        print("Cliente no encontrado.")

def crear_revision():
    id_auto = input("Ingrese la matricula del auto: ")
    fecha = input("Ingrese la fecha de la revisión: ")
    descripcion = input("Ingrese la descripción de la revisión: ")
    revision = Revision(id_auto, fecha, descripcion)
    Revision.create(revision)
    print("Revisión creada exitosamente.")

def leer_revision():
    id_revision = input("Ingrese el ID de la revisión: ")
    revision = Revision.read(id_revision)
    if revision:
        print(f"ID Revisión: {revision['id_revision']}")
        print(f"ID Auto: {revision['id_auto']}")
        print(f"Fecha: {revision['fecha']}")
        print(f"Descripción: {revision['descripcion']}")
    else:
        print("Revisión no encontrada.")

def actualizar_revision():
    id_revision = input("Ingrese el ID de la revisión a actualizar: ")
    revision_existente = Revision.read(id_revision)
    if revision_existente:
        fecha = input(f"Nuevo valor para fecha (actual: {revision_existente['fecha']}): ")
        descripcion = input(f"Nuevo valor para descripción (actual: {revision_existente['descripcion']}): ")
        revision = Revision(id_revision, revision_existente['id_auto'], 
                            fecha if fecha else revision_existente['fecha'],
                            descripcion if descripcion else revision_existente['descripcion'])
        Revision.update(revision)
        print("Revisión actualizada exitosamente.")
    else:
        print("Revisión no encontrada.")

def eliminar_revision():
    id_revision = input("Ingrese el ID de la revisión a eliminar: ")
    Revision.delete(id_revision)
    print("Revisión eliminada exitosamente.")

def ver_revisiones():
    revisiones = Revision.verTodo()
    if revisiones:
        for revision in revisiones:
            print(f"--Revisión--")
            print(f"ID Revisión: {revision['id_revision']}")
            print(f"ID Auto: {revision['id_auto']}")
            print(f"Fecha: {revision['fecha']}")
            print(f"Descripción: {revision['descripcion']}")
    else:
        print("No se encontraron revisiones.")

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Seleccione una opción: ")

        if opcion_principal == '1':
            while True:
                mostrar_menu_autos()
                opcion_autos = input("Seleccione una opción: ")
                if opcion_autos == '1':
                    crear_auto()
                elif opcion_autos == '2':
                    buscar_auto()
                elif opcion_autos == '3':
                    actualizar_auto()
                elif opcion_autos == '4':
                    eliminar_auto()
                elif opcion_autos == '5':
                    ver_autos()
                elif opcion_autos == '6':
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

        elif opcion_principal == '2':
            while True:
                mostrar_menu_clientes()
                opcion_clientes = input("Seleccione una opción: ")
                if opcion_clientes == '1':
                    registrar_cliente()
                elif opcion_clientes == '2':
                    ver_cliente()
                elif opcion_clientes == '3':
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

        elif opcion_principal == '3':
            while True:
                mostrar_menu_revisiones()
                opcion_revisiones = input("Seleccione una opción: ")
                if opcion_revisiones == '1':
                    crear_revision()
                elif opcion_revisiones == '2':
                    leer_revision()
                elif opcion_revisiones == '3':
                    actualizar_revision()
                elif opcion_revisiones == '4':
                    eliminar_revision()
                elif opcion_revisiones == '5':
                    ver_revisiones()
                elif opcion_revisiones == '6':
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

        elif opcion_principal == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
