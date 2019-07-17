import mysql.connector
from clase.user import *

class AdminUsers:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		self.__cursor = self.__cnx.cursor()

	def createUser(self, user):
		query = "INSERT INTO user(name) VALUES ('%s')" %(user.getName())
		self.__cursor.execute(query)
		self.__cnx.commit()

	def updateUserName(self, user):
		query = "UPDATE users SET name ='%s'  where id_user = %i"(%user.getName(), user.getId())
		self.__cursor.execute(query)
		self.__cnx.commit()

	def updatePassword(self, user):
		query = "UPDATE users SET password ='%s'  where id_user = %i"(%user.getPassword(), user.getId())
		self.__cursor.execute(query)
		self.__cnx.commit()


	def deleteUser(self, user):
		query = "DELETE FROM users WHERE id_user=%i" %(user.getId())
		self.__cursor.execute(query)
		self.__cnx.commit()

	def getAll(self):
		query = "SELECT * from users"
		self.__cursor.execute(query)
		users_db = self.__cursor.fetchall()
		users = []
		for user in users_db:
			users.append(User(user[1], user[2]))
		return users

	def getById(self, user):
		query = "SELECT * from users WHERE id_user = %i" %(user.getId())
		self.__cursor.execute(query)
		user_db = self.__cursor.fetchone()
		user = ''
		if len(user_db) > 0:
			user = User(user_db[1], user_db[2])
		return user

	def cerrarConexion(self):
		self.__cursor.close()
		self.__cnx.close()