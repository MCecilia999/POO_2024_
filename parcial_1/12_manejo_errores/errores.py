#los errores de ejcucion en un lenguaje de programacion se presentan cuando existe una naomalia o error dentro de la ejecucion del codigo lo cual proboca
#que se detenga la ejecucion delSw con el control y manejo de exepciones sera posible minimizar o evitar la interrupcion del programa
#devido a una exepcion

#ejemplo 1: cuando una variable no se genera


try:
    nombre=input("Introduce el nombre completo de una persona:")   
    if len(nombre)>0:
        nombre_usuario="El nombre completo del usuarioes: "+nombre

    print(nombre_usuario)
except:
    print("Es necesario introducirun nombre de usuario, verifique por favor")

x=3+4
print("El valor de x es:"+str(x))

#Ejemplo 2: cuando se solicita un numero y se ingresa otra cosa

try:
    numero=int(input("Ingrese un numero entero:"))

    if numero>0:
        print("soy numero emtero positivo")
    elif numero==0:
        print("Soy un numero entero neutro")
    else:
        print("Soy numero entero negativo")
except ValueError:
    print("Introduce un valor entero numerico")

#Ejemplo3: generar multiples exepcciones

try:
    numero=int(input("Ingrese un numero:"))

    print("El cuadrado de el numero es:" +str(numero*numero))
except ValueError:
    print("Introduce un valor numerico")
except TypeError:
    print("Se deve convertir el numero a entero")
else:
    print("No se presentaron errores de ejecucion")
finally:
    print("Termine la ejecucion")

