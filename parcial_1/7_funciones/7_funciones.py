#Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeñoque cumple una funcion especifica. la funcion se puede reutilizar con el simple hecho de inbocarla es decir


def nombredeMifuncion(parametros):
    #bloque o conjunto de instrucciones
    print ("Bloque o conjunto de instrucciones")

nombredeMifuncion()

#Las funciones pueden ser de 4 tipos
#1 Funciones que no resibe parametros y no egresa valor
#2 Funcion que no recibe parametros y regresa valor
#3 Funciones que no resibe parametros y NO regresa valor
#4 Funciones que resibe parametros y regresa valor 


#Ejemplo 1: 1 crear una funcion para imprimir nombres de personas
#1 Funciones que no resibe parametros y no egresa valor

def solicitarNombres():
    nombre=input("Ingresa el nombre completo: ")

solicitarNombres()

#Ejemplo 2: Funcion que no recibe parametros y regresa valor

def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma()

#Ejemplo 3: sumar 2 numeros redgresando un valor

def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma

resultado_suma=suma()
print(f"La suma es: {resultado_suma}")

#Ejemplo 4: realizar suma
#Funciones que resibe parametros y regresa valor

def suma (n1,n2):
    suma=n1+n2
    print(suma)


n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)

#Ejemplo 5:

def suma (n1,n2):
    suma=n1+n2
    return suma

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")

#Ejamplo 3 crear un programa que solicite atraves de una funcion la siguente informacion:
#Nombre del paciente, edad, estatura, tipo de sangre. 
#utillizar los 4 tipos de funciones  |

def infoPaciente():
    nombre = input("Escribe el nombre del paciente")
    edad = input("Escribe la edad del paciente")
    eatatura = input("Escribe la  estatura del paciente")
    tipoSangre = input("Escribe el tipo de sangre del paciente")
    return(f"Nombre: ")


valor= infoPaciente()
#Recibe parametros pero no regresa valor
def infoPaciente2(nom, edad, est, sandre):
    return
