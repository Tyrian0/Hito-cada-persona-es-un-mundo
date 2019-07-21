import sys
sys.path.append('../')

import mysql.connector
from logica.User import *
from logica.Experience import *
from logica.Recomendation import *
from logica.Review import *
from AdminReview import *
from AdminRecomendation import *

class AdminUser:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		self.__cursor = self.__cnx.cursor()

	# Usado al tratar de registrarse: si el nombre de usuario ya existe, no lo añadirá a la BBDD
	def addUser(self, user):
		if user == None or type (user) != User:
			raise UserNoValidException()
		retrievedUser = self.getByUsername(user.getName())
		if retrievedUser is None:
			query = "INSERT INTO users(name, password) VALUES ('%s', '%s')" \
			%(user.getName().replace("'", "''"), user.getPassword().replace("'", "''"))
			self.__cursor.execute(query)
			self.__cnx.commit()
		else:
			return 'This username already exists!'

	# Chequea si el nombre de usuario existe en la BBDD
	def getByUsername(self, name):
		query = "SELECT * from users WHERE name = '%s'" %(str(name).replace("'", "''"))
		user = self.retrieveUser(query)
		if user is not None and type (user) == User:
			return user
		else:
			"This username doesn't exist!"		

	# Chequea si existe el nombre de usuario con esta contraseña en la BBDD
	def getByUsernameAndPassword(self, name, password):
		query = "SELECT * from users WHERE name = '%s' AND password = '%s'" \
		%(str(name).replace("'", "''"), str(password).replace("'", "''"))
		user = self.retrieveUser(query)
		if user is not None and type (user) == User:
			return user
		else:
			"Ooops! Wrong password!"

	def retrieveUser(self, query):
		adminReview = AdminReview()
		adminRecomendation = AdminRecomendation()
		self.__cursor.execute(query)
		user_db = self.__cursor.fetchone()
		if user_db is None:
			return
		else:
			user = User(user_db[1], user_db[2], [], [], user_db[0])
			reviews = adminReview.getReviewsFromUser(user)
			recomendations = adminRecomendation.getRecomendationsFromUser(user)
			user = User(user_db[1], user_db[2], reviews, recomendations, user_db[0])
			return user

	def closeConnection(self):
		self.__cursor.close()
		self.__cnx.close()

	def deleteAll(self):
		query = "DELETE FROM users"
		self.__cursor.execute(query)
		self.__cnx.commit()

	# def getAll(self):
	# 	adminReview = AdminReview()
	# 	adminRecomendation = AdminRecomendation()
	# 	query = "SELECT * from users"
	# 	self.__cursor.execute(query)
	# 	users_db = self.__cursor.fetchall()
	# 	users = []
	# 	for user_db in users_db:
	# 		user = User(user_db[1], str(user_db[2]), [], [], user_db[0])
	# 		reviews = adminReview.getReviewsFromUser(user)
	# 		recomendations = adminRecomendation.getRecomendationsFromUser(user)			
	# 		users.append(User(user_db[1], str(user_db[2]), reviews, recomendations, user_db[0]))
	# 	return users

	# def updateName(self, user):
	# 	query = "UPDATE users SET name ='%s'  where id_user = %i" %(user.getName(), user.getId())
	# 	self.__cursor.execute(query)
	# 	self.__cnx.commit()

	# def updatePassword(self, user):
	# 	query = "UPDATE users SET password ='%s'  where id_user = %i" %(user.getPassword(), user.getId())
	# 	self.__cursor.execute(query)
	# 	self.__cnx.commit()

	# def deleteUser(self, user):
	# 	query = "DELETE FROM users WHERE id_user=%i" %(user.getId())
	# 	self.__cursor.execute(query)
	# 	self.__cnx.commit()