#hacer un programa que solicite numeros indefinitivamente hasta que se intodusca el 111 y salir del programa


while True:
        numero = int(input("Ingrese un número (o ingrese 111 para salir): "))
        if numero == 111:
            print("Saliendo del programa...")
            break
        else:
            print(f"El número ingresado es: {numero}")


