#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aprobraron y cuantos no

aprobados = 0
no_aprobados = 0

for i in range(1, 16):
    calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
    
    if calificacion >= 70:
        aprobados += 1
    else:
        no_aprobados += 1

# Imprimir el resultado
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos no aprobados: {no_aprobados}")