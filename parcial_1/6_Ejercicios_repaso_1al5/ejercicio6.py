#Mostrar todas las tablas del 1 al 10 
#Mostrar el titulo de la tabla y luego las multiplicaciones del 1 al 10

inicio = 1
fin = 10

print("Tabla de Multiplicar")


for multiplicando in range(inicio, fin + 1):
   
    print(f"\nTabla del {multiplicando}:")
    
   
    for multiplicador in range(inicio, fin + 1):
        
        producto = multiplicando * multiplicador
      
        print(f"{multiplicando} x {multiplicador} = {producto}")