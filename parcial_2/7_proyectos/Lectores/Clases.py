

class Lectores:
    def _init_(self,nombre,direccion,telefono):
        self.nombre =nombre
        self.direccion = direccion
        self.telefonp = telefono
    
    def reservar(self):
        print(f"{self.nombre}  reservo un libro.")
    
    def entregar(self):
        print(f"{self.nombre}  entrego un libro.")


class Estudiante(Lectores):
    def _init_(self, nombre, direccion, telefono, carrera, matricula):
        super()._init_(nombre, direccion, telefono)
        self.carrera = carrera
        self.matricula = matricula
    
    def reservar(self):
        print(f"El Estudiante {self.nombre} de carrera {self.carrera}  reservo un libro.")
    
    def entregar(self):
        print(f"El Estudiante {self.nombre} con matrícula {self.matricula}  entrego un libro.")
   

class Docentes(Lectores):
    def _init_(self, nombre, direccion, telefono, modalidad, num_empleado):
        super()._init_(nombre, direccion, telefono)
        self.modalidad = modalidad
        self.num_empleado = num_empleado
    
    def reservar(self):
        print(f"El Docente {self.nombre} de la modalidad {self.modalidad} reservo un libro.")
    
    def entregar(self):
        print(f"El Docente {self.nombre} con número de empleado {self.num_empleado} entrego un libro.")
    