import sys
sys.path.append('../')

import mysql.connector
from logica.Recomendation import *
from logica.Rating import *
from logica.User import *

class AdminRecomendation:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		
	def __getCursor(self):
		return self.__cnx.cursor()		

	def addRecomendation(self, recomendation, user):
		if recomendation == None or type (recomendation) != Recomendation:
			raise RecomendationNoValidException()			
		if user == None or type (user) != User:
			raise UserNoValidException()
		cursor = self.__getCursor()		
		query = "INSERT INTO recommendations(id_exp, id_user, rating) VALUES (%i, %i, %f)" \
		%(recomendation.getExperience().getId(), user.getId(), recomendation.getRating().getValue())
		cursor.execute(query)
		self.__cnx.commit()
		cursor.close()

	def getRecomendationsFromUser(self, user):
		if user == None or type (user) != User:
			raise UserNoValidException()
		cursor = self.__getCursor()
		query = "SELECT r.rating, e.name, e.id_exp, t.name, t.id_type from recommendations r " \
				"JOIN users u ON u.id_user = r.id_user " \
				"JOIN experiences e ON e.id_exp = r.id_exp " \
				"JOIN types_experiences t ON e.id_type = t.id_type " \
				"WHERE u.id_user = %i" %(user.getId())
		cursor.execute(query)
		recomendations_db = cursor.fetchall()
		recomendations = []
		for recomend_db in recomendations_db:
			experience = Experience(recomend_db[1], recomend_db[3], recomend_db[2])
			rating = Rating(recomend_db[0])
			recomendation = Recomendation(experience, rating)
			recomendations.append(recomendation)
		cursor.close()
		return recomendations

	def closeConnection(self):
		self.__cnx.close()

	def deleteAll(self):
		cursor = self.__getCursor()
		query = "DELETE FROM recommendations"
		cursor.execute(query)
		self.__cnx.commit()
		cursor.close()

	# def getAll(self):
	# 	query = "SELECT * from recommendations"
	# 	cursor.execute(query)
	# 	recomendations_db = cursor.fetchall()
	# 	recomendationss = []
	# 	for recomendation in recomendations_db:
	# 		experience = AdminExperience.getById(recomendation[0])
	# 		recomendations.append(recomendation(experience, recomendation[2]))
	# 	return recomendations