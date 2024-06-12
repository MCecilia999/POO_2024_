def agregar_pelicula(peliculas):
    pelicula = input("Ingrese el nombre de la película que desea agregar: ")
    peliculas.append(pelicula)
    print(f"'{pelicula}' ha sido agregada a la lista.")

def eliminar_pelicula(peliculas):
    pelicula = input("Ingrese el nombre de la película que desea remover: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print(f"'{pelicula}' ha sido eliminada de la lista.")
    else:
        print(f"'{pelicula}' no se encuentra en la lista.")

def actualizar_peliculas(peliculas):
    if peliculas in peliculas:
        actualizar_peliculas[peliculas] = peliculas
    else:
        print(f"La clave '{peliculas}' no existe en el diccionario.")

def consultar_peliculas(peliculas):
    if peliculas:
        print("\nLista de películas:")
        for i, pelicula in enumerate(peliculas, start=1):
            print(f"{i}. {pelicula}")
    else:
        print("\nNo hay películas en la lista.")