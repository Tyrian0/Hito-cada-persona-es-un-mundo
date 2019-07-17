import mysql.connector
from clases.cd import Cd
from clases.discografica import Discografica
from clases.genero import Genero

class AdminCd:
    def __init__(self):
        #self.__cnx = mysql.connector.connect(user='root', password='lenovo1', port='3305', host='localhost', database='discoteca')
        self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='discoteca')

    def crear(self, cd):
        cursor = self.__cnx.cursor()
        cursor.execute("INSERT INTO cds (nombre, anyo, idDiscografica) VALUES ('%s', '%s', %d)" \
            %(cd.getNombre(), cd.getAnyo(), cd.getDiscografica().getId()))
        cd.setId(cursor.lastrowid)
        self.__cnx.commit()      
        cursor.close()
        for genero in cd.getGeneros():        
            self.__modificar("INSERT INTO cds_generos (idCD, idGenero) Values ('%i', '%i')" %(cd.getId(), genero.getId()))

    def actualizar(self, cd):
        self.__modificar("UPDATE cds SET nombre = '%s', anyo = '%s', idDiscografica = %d WHERE id = %i" \
            %(cd.getNombre(), cd.getAnyo(), cd.getDiscografica().getId(), cd.getId()))
        self.__modificar("DELETE FROM cds_generos WHERE idCD = %i" % (cd.getId()))
        for genero in cd.getGeneros():        
            self.__modificar("INSERT INTO cds_generos (idCD, idGenero) Values ('%i', '%i')" %(cd.getId(), genero.getId()))

    def borrar(self, cd):
        self.__modificar("DELETE FROM cds_generos WHERE idCD = %i" % (cd.getId()))
        self.__modificar("DELETE FROM cds WHERE id = %i" % (cd.getId()))

    def getAll(self):
        cds_tabla = self.__consultar("""SELECT c.id, c.nombre, c.anyo, d.id, d.nombre  FROM cds c
                                        JOIN discograficas d ON d.id = c.idDiscografica""")
        cds = []
        for cd in cds_tabla:
            generos_tabla = self.__consultar("""SELECT g.*  FROM generos g
                                                JOIN cds_generos cdg ON cdg.idGenero = g.id
                                                WHERE cdg.idCD = '%d'""" % cd[0])
            generos = []
            for genero in generos_tabla:
                generos.append(Genero(genero[1], genero[0]))
            cds.append (Cd(cd[1],cd[2], Discografica(cd[4], cd[3]), cd[0], generos))
        return cds
    
    def __consultar(self, query):
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado

    def __modificar(self, query):
        cursor = self.__cnx.cursor()
        cursor.execute(query)
        self.__cnx.commit()       
        cursor.close()


    def getById(self, id):
        pass

    def cerrarCnx(self):
        self.__cnx.close() 
