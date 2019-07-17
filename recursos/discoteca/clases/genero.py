class Genero:
#constructor
    def __init__(self, nombre, id = None):
        self.setId(id)
        self.setNombre(nombre)

    def getId(self):
        return self.__id

    def setId(self, pId):
        self.__id = pId

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    #funcion string
    def __str__(self):
        #return str(self.__id)+ "\t" + self.__nombre
        return self.__nombre



