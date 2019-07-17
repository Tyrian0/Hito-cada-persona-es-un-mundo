import mysql.connector
from clase.genero import *

class AdminTypesExperiences:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		self.__cursor = self.__cnx.cursor()

	def addTypeExperience(self,name):
		query = "INSERT INTO types_experiences(name) VALUES ('%s')" %(name)
		self.__cursor.execute(query)
		self.__cnx.commit()

	def getAll(self):
		query = "SELECT * from types_experiences"
		self.__cursor.execute(query)
		types_experiences = self.__cursor.fetchall()
		return types_experiences

	def getById(self, id_type):
		query = "SELECT * from types_experiences WHERE id_type = %i" %(id_type)
		self.__cursor.execute(query)
		type_experience = self.__cursor.fetchone()
		return type_experience

	def getByName(self, name):
		query = "SELECT * from types_experiences WHERE name = '%s'" %(name)
		self.__cursor.execute(query)
		type_experience = self.__cursor.fetchone()
		return type_experience


	def cerrarConexion(self):
		self.__cursor.close()
		self.__cnx.close()