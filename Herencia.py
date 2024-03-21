class Bebida: 

    def __init__(self,nombre):
        self.__nombre = nombre

    def getObtenerNombre(self):
        return f"La bebida es {self.__nombre}" ##Concatenar con f#
    
    
##bebida = Bebida("Agua")
##print(bebida.__nombre)    
    
class Cerveza(Bebida): ##Herencian del metodo de la clase padre 
    def __init__(self,nombre,marca,alcohol):
        super().__init__(nombre)
        self.__marca = marca
        self.__alcohol = alcohol
        
    def getObtenerNombre(self):
        return f"{super().getObtenerNombre()} de la marca {self.__marca} con grado de alcohol {self.__alcohol}" ## obtiene el nombre de la clase padre 
        
cerveza=Cerveza("poker","Bavaria",4.0)
print(cerveza.getObtenerNombre())
