#Hacer un programa que resuelva lo siguente 
#¿cuanto es el X por ciento de X numero?


def calcular_porcentaje():
    numero = float(input("Ingrese el número: "))
    porcentaje = float(input("Ingrese el porcentaje (sin el signo de porcentaje %): "))
    resultado = (porcentaje / 100) * numero
    print(f"{porcentaje}% de {numero} es: {resultado}")

calcular_porcentaje()
