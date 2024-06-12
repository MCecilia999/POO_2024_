#2.- Escribir un programa  que añada valores a una lista mientras que su longitud 
# sea menor a 120, y luego mostrar la lista: Usar un while y for
numeros=[]

contador = 1
while len(numeros) < 120:
    numeros.append(contador)
    contador += 1

print("Lista de números:")

for numero in numeros:
    print(numero, end=" ")
print("\n")
