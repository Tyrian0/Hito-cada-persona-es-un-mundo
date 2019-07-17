import mysql.connector
from clases.discografica import Discografica

class AdminDiscografica:
    def __init__(self):
        #self.__cnx = mysql.connector.connect(user='root', password='lenovo1', port='3305', host='localhost', database='discoteca')
        self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='discoteca')

    def __ejecutar(self, query):
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        self.__cnx.commit()       
        cursor.close()
        return res

    def crear(self, discografica):
        query = ("INSERT INTO discograficas (nombre) VALUES ('%s')" % discografica.getNombre())
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        self.__cnx.commit()       
        cursor.close()
    def actualizar(self, discografica):
        query = "UPDATE discograficas SET nombre = '%s' WHERE id = %i" % (discografica.getNombre(), discografica.getId())
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        self.__cnx.commit()       
        cursor.close()
    def borrar(self, discografica):
        query = "DELETE FROM discograficas WHERE id = %i" % (discografica.getId())
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        self.__cnx.commit()       
        cursor.close()
    def getAll(self):
        query = ("SELECT * FROM discograficas")
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        discograficas_tabla = cursor.fetchall()
        discograficas = []
        for discografica in discograficas_tabla:
            discograficas.append (Discografica(discografica[1],discografica[0]))
        cursor.close()
        return discograficas
        
    def getById(self, id):
        pass
    def cerrarCnx(self):
        self.__cnx.close() 
