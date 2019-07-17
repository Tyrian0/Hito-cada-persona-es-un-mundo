import mysql.connector
from clases.genero import Genero

class AdminGenero:
    def __init__(self):
        #self.__cnx = mysql.connector.connect(user='root', password='lenovo1', port='3305', host='localhost', database='discoteca')
        self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='discoteca')

    def __ejecutar(self, query):
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        self.__cnx.commit()       
        cursor.close()
        return res

    def crear(self, genero):
        query = ("INSERT INTO generos (nombre) VALUES ('%s')" % genero.getNombre())
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        self.__cnx.commit()       
        cursor.close()
        
    def actualizar(self, genero):
        query = "UPDATE generos SET nombre = '%s' WHERE id = %i" % (genero.getNombre(), genero.getId())
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        self.__cnx.commit()       
        cursor.close()

    def borrar(self, genero):
        query = "DELETE FROM generos WHERE id = %i" % (genero.getId())
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        self.__cnx.commit()       
        cursor.close()

    def getAll(self):
        query = ("SELECT * FROM generos")
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        generos_tabla = cursor.fetchall()
        generos = []
        for genero in generos_tabla:
            generos.append (Genero(genero[1],genero[0]))
        cursor.close()
        return generos
        
    def getById(self, id):
        pass
    def cerrarCnx(self):
        self.__cnx.close() 
