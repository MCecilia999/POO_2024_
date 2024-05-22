#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

num1= int(input("Escribe un número: "))

num2= int(input("Escribe un numero: "))

for numero in range (num1+1, num2):
    print (numero)