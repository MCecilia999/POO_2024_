#Crear una lista y un diccionario con el contenido de esta tabla: 

#ACCION              TERROR        DEPORTES
#MAXIMA VELOCIDAD    LA MONJA       ESPN
#ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#RAPIDO Y FURIOSO I  LA MALDICION   ACCION
#imprimir la información

tabla = [
    ["ACCION", "TERROR", "DEPORTES"],
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

tabla_diccionario = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

def imprimir_lista(lista):
    for fila in lista:
        print("\t".join(fila))

def imprimir_diccionario(diccionario):
    for key, value in diccionario.items():
        print(f"{key}: {', '.join(value)}")

print("Lista:")
imprimir_lista(tabla)

print("\nDiccionario:")
imprimir_diccionario(tabla_diccionario)