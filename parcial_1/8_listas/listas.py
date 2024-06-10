
import os
"""
list (Array)
son coleciones o conjuntos de datos/valores bajo
un mismo nombre para acceder alos valores se hace 
con un indice numerico
nota:sus valores si son modificados
la listas es una coleccion ordenada y modificable permite miembros duplicados

"""

# #1 Ejemplo: crear una lista de numeros e imprimir el contenido
# numeros=[23,24]
# print(numeros)

# #recorrer con siclo for
# for i in numeros:
#     print(i)

# #recorrer con siclo while
# i=0

# while i<=len(numeros)-1:
#     print(numeros[i])
#     i+=1

#2 Ejamplo: crear una lista de palabrasy posterior mente buscar la coincidencia de una palabra

# palabras=["hola", "como", "estas",]
# print(palabras)

# palabras_buscar=input("Ingresa la palabra buscar")

# repetir=True

# for i in palabras:
#     if i ==palabras_buscar:
#         print(f"Encontre la palabra a buscar en la poocicion {palabras_buscar} en la posicion{palabras.index(i)}")
#         encontre=True

# while i<len(palabras):
#     if palabras[i]==palabras_buscar :
#         print(f"")
#         repetir=False








# #Ejemplo 3: agregar y eliminar elementos de una lista
# #os system ("clear")

# numeros=[23,34,23]
# print(numeros)

# #agregar un elemento
# numeros.append(100) #agrega el elemento al final de la lista
# print(numeros)
# numeros.insert(3,200)  #agrega el elmento en la pocicion indicada
# print(numeros)

# #eliminar un elementos
# numeros.remove(100)   #indicar el elemento a borrar
# print(numeros)
# numeros.pop(2)    #indicar la pocicion del el elemento a borrar 
# print(numeros)

#Ejamplo4: crear una lista multilinea (matriz) para agregar nombres y numeros telefonicos

# agenda=[
#   ["Carlos", 6181234567],
#   ["leo",6671234567],
#   ["sebastian",6182341234],
#   ["pedro",6171236789],
# ]

# print(agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1}.-{i}")


#Ejemplo5:

def esperarTecla():
    print("Oprima cualquier tecla para continuar ...")
    input() 


Peliculas=[]
Pelicula=input("Pelicula")

def agregarPelicula(Pelicula):
    Peliculas.append(Pelicula)

def removerPelicula(Pelicula):
    Peliculas.remove(Pelicula)

def consultarPelicula(Pelicula):
    for i in Peliculas:
        if Pelicula in Peliculas:
            print(f"{Peliculas.index(i)+1}.-{i}")
i=True
while i:
    os.system("Clear")
    print(f"========== \n Finepolis \n=============")
    print("1.- Agregar")
    print("2.- Remover")
    print("3.- consultar")
    print("5.- Salir")
    opcion= input("Elige una opción ").upper()
    if opcion== "1" or opcion=="Agregar":
        insertarPelicula()
        