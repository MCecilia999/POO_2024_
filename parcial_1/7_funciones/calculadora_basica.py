import os
#print("\n\t..::CALCULADORA BASICA::..\n1, -Suma \n2 ,-Resta")
"""
i=True
while i:
    print("..::Calculadora Basica::..")

    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion")
    print("4.- Divicion")
    print("5.- Saliste")
    opcion=input("Elije una opcion").upper()

    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        n1=int(input("Numero 1: "))
        n2=int(input("Numero 2: "))
        suma=n1+n2
        print(f"{n1} + {n2} = {suma}")

    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        n1=int(input("Numero 1: "))
        n2=int(input("Numero 2: "))
        resta=n1-n2
        print(f"{n1} - {n2} = {resta}")

    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
        n1=int(input("Numero 1: "))
        n2=int(input("Numero 2: "))
        multiplicacion=n1*n2
        print(f"{n1} * {n2} = {multiplicacion}")

    elif opcion=="4" or opcion=="/" or opcion=="DIVICION":
        n1=int(input("Numero 1: "))
        n2=int(input("Numero 2: "))
        divicion=n1/n2
        print(f"{n1} / {n2} = {divicion}")
    else:
        print("Saliste")
        i=False
"""

#..::Funciones::..

def SolicitarNumeros():
    global n1,n2
    n1=int(input("Número 1: "))
    n2=int(input("Número 2: "))

def OperacionesArit(n1,n2):
    global i
    #..::Suma::..
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        suma=n1+n2
        return(f"{n1} + {n2} = {suma}")

    #..::Resta::..
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        resta=n1-n2
        return(f"{n1} - {n2} = {resta}")

    #..::Multiplicación::..
    elif opcion=="3" or opcion=="x" or opcion=="MULTIPLICACION":
        multiplicacion=n1*n2
        return(f"{n1} x {n2} = {multiplicacion}")

    #..::Divición::..
    elif opcion=="4" or opcion=="/" or opcion=="DIVICION":
        divicion=n1/n2
        return(f"{n1} / {n2} = {divicion}")
    else:
        print("Saliste")
        i=False

i=True
while i:
    print(f"========== \n Calculadora Básica \n=============")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- Divición")
    print("5.- Salir")
    opcion= input("Elige una opción ").upper()

    SolicitarNumeros()
    print(OperacionesArit(n1,n2))



def solicitarNumeros():
  global n1,n2  
  n1=int(input("Numero #1: "))
  n2=int(input("Numero #2: "))
   

def operacionAritmetica(num1,num2,opcion):  
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
      return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
     return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
     return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
     return f"{n1}/{n2}={n1/n2}"  
    else:  
     opcion=False    
     return "Terminaste la ejecucion del SW"

    
opcion=True    
while opcion:
 os.system("clear")
 print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
 opcion=input("\t Elige una opción: ").upper()



if opcion!="5":
    solicitarNumeros()
    print(operacionAritmetica(n1,n2,opcion))
else:
   print("Saliste")
   opcion=False

   
