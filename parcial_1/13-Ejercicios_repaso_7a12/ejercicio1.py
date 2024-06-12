#1.-Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

# a.- Recorrer la lista y mostrarla
 #b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 #c.- ordenarla y mostrarla
 #d.- mostrar su longitud
 #e.- buscar algun elemento que el usuario pida por teclado

numeros=[2,4,6,8,10,12,14,16]

try:
    for numero in numeros:
        print(numero, end=" ")
except Exception as e:
    print(f"Error al recorrer la lista: {e}")
print("\n")



