import sys
sys.path.append('../')

import mysql.connector
from logica.Recomendation import *
from logica.Rating import *

class AdminRecomendation:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		self.__cursor = self.__cnx.cursor()

	def addRecomendation(self, recomendation, user):
		query = "INSERT INTO recommendations(id_exp, id_user, rating) VALUES (%i, %i, %f)" \
		%(recomendation.getExperience().getId(), user.getId(), recomendation.getRating().getValue())
		self.__cursor.execute(query)
		self.__cnx.commit()

	def getAll(self):
		query = "SELECT * from recommendations"
		self.__cursor.execute(query)
		recomendations_db = self.__cursor.fetchall()
		recomendationss = []
		for recomendation in recomendations_db:
			experience = AdminExperience.getById(recomendation[0])
			recomendations.append(recomendation(experience, recomendation[2]))
		return recomendations

	def getRecomendationsFromUser(self, user):
		query = "SELECT r.rating, e.name, e.id_exp, t.name, t.id_type from recommendations r " \
				"JOIN users u ON u.id_user = r.id_user " \
				"JOIN experiences e ON e.id_exp = r.id_exp " \
				"JOIN types_experiences t ON e.id_type = t.id_type " \
				"WHERE u.id_user = %i" %(user.getId())
		self.__cursor.execute(query)
		recomendations_db = self.__cursor.fetchall()
		print(recomendations_db)
		# for recomendation_db in recomendations_db:
		# 	recomendation = recomendation()

	# def getById(self, id_recomendation):
	# 	query = "SELECT * from recomendations WHERE id_user =%i and id_exp = %i" %(id_recomendation[0], id_recomendation[1])
	# 	self.__cursor.execute(query)
	# 	recomendation_db = self.__cursor.fetchone()
	# 	recomendation = ''
	# 	if len(recomendation_db) > 0:
	# 		recomendation = recomendation(recomendation_db[1], recomendation_db[2])
	# 	return user

	def closeConnection(self):
		self.__cursor.close()
		self.__cnx.close()