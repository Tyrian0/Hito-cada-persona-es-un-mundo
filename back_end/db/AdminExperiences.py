import mysql.connector
from AdminTypesExperiences import *

class AdminExperiences:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		self.__cursor = self.__cnx.cursor()

	def addExperience(self, experience):
		typeName = experience.getType()
		type = AdminTypeExperiences.getByName(typeName)
		idType = type[0]
		query = "INSERT INTO experience(name,id_type) VALUES ('%s',%i)" %(experience.getName(),idType)
		self.__cursor.execute(query)
		self.__cnx.commit()


	def getAll(self):
		query = "SELECT * from experiences"
		self.__cursor.execute(query)
		experiences_db = self.__cursor.fetchall()
		experiences = []
		for experience in experiences_db:
			experiences.append(Experience(experience[1], experience[2], experience[0]))
		return experiences

	def getById(self, id_exp):
		query = "SELECT * from experiences WHERE id_exp = %i" %(id_exp)
		self.__cursor.execute(query)
		experience_db = self.__cursor.fetchone()
		experience = ''
		if len(experience_db) > 0:
			experience = Experience(experience_db[1], experience_db[2], experience_db[0])
		return experience

	def cerrarConexion(self):
		self.__cursor.close()
		self.__cnx.close()