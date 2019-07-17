class Cd:
#constructor
    def __init__(self, nombre, anyo, discografica, id = None, generos=[]):
        self.setId(id)
        self.setAnyo(anyo)
        self.setNombre(nombre)
        self.setDiscografica(discografica)
        self.setGeneros(generos)

    def getId(self):
        return self.__id

    def setId(self, pId):
        self.__id = pId

    def getAnyo(self):
        return self.__anyo

    def setAnyo(self, anyo):
        self.__anyo = anyo

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDiscografica(self):
        return self.__discografica

    def setDiscografica(self, discografica):
        self.__discografica = discografica

    def getGeneros(self):
        return self.__generos

    def setGeneros(self, generos):
        self.__generos = generos

    def addGenero(self, genero):
        self.__generos.append(genero)

    def removeGenero(self, genero):
        self.__generos.remove(genero)

    #funcion string
    def __str__(self):
        #return str(self.__id)+ "\t" + self.__nombre
        generos = ""
        for genero in self.__generos:
            generos += str(genero) + ", "
        generos = generos[0:len(generos)-2] #Eliminamos el último ", "
        return "%-45s\t%s\t%-20s\t%s" %(self.__nombre, self.__anyo, str(self.__discografica), generos)




