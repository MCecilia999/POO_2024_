#hacer un programa que muestre todos los numeros inpares entre dos numeros que decida el usuario

num1= int(input("Escribe un número: "))

num2= int(input("Escribe un numero: "))

for numero in range(num1, num2):
    if numero % 2 != 0:
        print(numero)