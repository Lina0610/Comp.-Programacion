# Clase 1: persona  atributos nombr y edad y un metodo saludar() "saludobasico":
# Herencia de 2:Estudiante a Persona , atributo adicional carrera 
# Metodo para imprimir la informacion 
# Atributo para contar el numero total de estudiantes 
# Atributo estudiantes creados 
# Clase 3: Herencia multiple, metodo con parametros adicionales 
# Integrantes: Lina Ballesteros y Jeanpier Rodriguez

class Persona:
    total_ingresados=0
    
    def __init__(self,nombre,edad): #atributos
        self.nombre =nombre
        self.edad= edad
        Persona.total_ingresados +=1 #aumenta el contador dependiendo el numero de personas ingresadas
        
    def saludar(self): #metodo
        print ( f" Bienvenido al sistema Ingreso a la U, tu nombre es: {self.nombre} y tu edad es: {self.edad} años")
    
class Estudiante(Persona):
    
    total_est_ingresados = 0
    
    def __init__(self, nombre, edad,carrera,semestre):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.semestre = semestre
        Estudiante.total_est_ingresados +=1
    
    def mostrar__informacion(self):
        print( f" El nombre ingresado es {self.nombre}, la edad registrada es {self.edad} y esta matriculado en la carrera {self.carrera} con ubicacion semestral {self.semestre}")
    
class Administrativo(Persona):
    
    total_admin__ingresados=0
    
    def __init__(self, nombre, edad,areaTrabajo,horario):
        super().__init__(nombre, edad)
        self.areaTrabajo = areaTrabajo
        self.horario = horario
        Administrativo.total_admin__ingresados +=1
    
    def  mostrar__informacion(self):
        print (f" El nombre del administrativo registrado es: {self.nombre}, con una edad de {self.edad} , ubicado en el área {self.areaTrabajo} y con un horario  {self.horario}")
        
# Personas ingresadas 
persona1 = Persona("Maria del Carmen",20)
persona1.saludar()


# Estudiantes Ingresados 
estudidante1 = Estudiante("Juan Salamanca",22,"Administracion",5)
estudidante1.mostrar__informacion()

#Administrativo 
administrativo1 = Administrativo("Ana Suarez",45,"Secretaria","Nocturno")
administrativo1.mostrar__informacion()

print(f"Total de personas: {Persona.total_ingresados}")
print(f"Total de estudiantes: {Estudiante.total_est_ingresados}")
print(f"Total de administrativos: {Administrativo.total_admin__ingresados}")
        
    
    
    
    