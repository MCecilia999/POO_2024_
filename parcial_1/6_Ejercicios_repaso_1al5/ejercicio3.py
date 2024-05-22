#Escribe un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales resolverlo con while y for

contador = 1
while contador <= 60:

    #cuadrado = contador ** 2
    #print(f"El cuadrado de {contador} es: {cuadrado}")
    
    

    for contador in range(1, 61):
        cuadrado = contador ** 2
        print(f"El cuadrado de {contador} es: {cuadrado}")
        contador += 1