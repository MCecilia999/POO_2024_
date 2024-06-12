peliculas = ["Toy Story 2", "candy candy", "anabell"]

def AgregarPeli():
    movie = input("\t¡AGREGA UNA PELÍCULA NUEVA!\nIngrese el nombre de la película: ")
    peliculas.append(movie.capitalize())
    print(f"¡Se ha agregado {movie} con éxito!")
    input("Presione Enter para continuar...")

def RemovePeli():
    print("\t¡ELIMINA UNA PELÍCULA!")
    print(peliculas)
    movie = input("Ingrese el nombre de la película que desea remover: ").capitalize()
    if movie in peliculas:
        resp = input(f"¿Seguro de eliminar {movie}? (SI o NO): ").upper()
        if resp == "SI":
            peliculas.remove(movie)
            print(f"¡La película {movie} ha sido removida con éxito!")
        else:
            print("Operación cancelada.")
    else:
        print(f"{movie} no fue encontrada en nuestra lista")

    input("Presione Enter para continuar...")

def ConsultarPeli():
    print("\t¡CONSULTA LA CARTELERA ACTUALIZADA!")
    print(peliculas)
    input("Presione Enter para continuar...")

def BuscarPeli():
    print("\t¡BUSCA UNA PELÍCULA!")
    movie = input("Ingresa la película a buscar: ").capitalize()
    
    if movie in peliculas:
        index = peliculas.index(movie)
        print(f"La película '{movie}' se encuentra en la posición {index} de la lista.")
    else:
        print("La película no se encontró en la lista.")

    input("Presione Enter para continuar...")

def VaciarLista():
    global peliculas
    resp = input("¿Está seguro de vaciar la lista de películas? (SI o NO): ").upper()
    if resp == "SI":
        peliculas = []
        print("La lista de películas ha sido vaciada.")
    else:
        print("Operación cancelada.")
    input("Presione Enter para continuar...")

# Menú principal
while True:
    print("\n\t..:: GESTIONADOR DE PELÍCULAS ::..")
    print(" 1. Agregar película")
    print(" 2. Eliminar película")
    print(" 3. Consultar películas")
    print(" 4. Buscar película")
    print(" 5. Vaciar lista de películas")
    print(" 6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        AgregarPeli()
    elif opcion == "2":
        RemovePeli()
    elif opcion == "3":
        ConsultarPeli()
    elif opcion == "4":
        BuscarPeli()
    elif opcion == "5":
        VaciarLista()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


