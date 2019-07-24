import sys
sys.path.append('../')

import mysql.connector
from logica.User import *
from logica.Experience import *
from logica.Recomendation import *
from logica.Review import *

class AdminTypeExperience:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		
	def __getCursor(self):
		return self.__cnx.cursor()		

	def addTypeExperience(self, name):
		retrievedType = self.getByName(name)
		if retrievedType is None:
			cursor = self.__getCursor()
			query = "INSERT INTO types_experiences(name) VALUES ('%s')" \
			%(str(name).replace("'", "''"))
			cursor.execute(query)
			self.__cnx.commit()
			cursor.close()
		else:
			return 'Type of experience already exists!'

	def getByName(self, name):
		cursor = self.__getCursor()
		query = "SELECT * from types_experiences WHERE name = '%s'" \
		%(str(name).replace("'", "''"))
		cursor.execute(query)
		type_experience = cursor.fetchone()
		cursor.close()
		return type_experience

	def closeConnection(self):
		self.__cnx.close()

	def deleteAll(self):
		cursor = self.__getCursor()
		query = "DELETE FROM types_experiences"
		cursor.execute(query)
		self.__cnx.commit()
		cursor.close()

	# def getAll(self):
	# 	query = "SELECT * from types_experiences"
	# 	cursor.execute(query)
	# 	types_experiences = cursor.fetchall()
	# 	return types_experiences

	# def getById(self, id_type):
	# 	query = "SELECT * from types_experiences WHERE id_type = %i" %(id_type)
	# 	cursor.execute(query)
	# 	type_experience = cursor.fetchone()
	# 	return type_experience