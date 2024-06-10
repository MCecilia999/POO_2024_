Paises=["Mexico", "USA", "Brasil", "Japon"]
numeros=[23,100,3.1416,0.100]
varios=["Hola", True, 100,10.22]

#ordenar la lista
print=(Paises)
Paises.sort()
print(Paises)

print=(numeros)
Paises.sort()
print(numeros)

#agregar elementos
print(numeros)
numeros.insert(len(numeros), 100)
print(numeros)
numeros.append(100)

#eliminar numeros
print(numeros)
numeros.pop(2)
print(numeros)
numeros.remove(100)

#Buscar dentro de una lista un dato
encontrar="Brasil" in Paises
print(encontrar)

#Dar la vuelta 
print(varios)
varios.reverse()
print(varios)

#Unir lista
print(Paises)
Paises.extend(numeros)
print(Paises)

#vaciar lista
print(varios)
varios.clear()
print(varios)

