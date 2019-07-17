import mysql.connector
from clase.user import *

class AdminReviews:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		self.__cursor = self.__cnx.cursor()

	def addReview(self, review, user):
		query = "INSERT INTO review(id_exp,id_user,rating) VALUES (%i, %i, %f)" /n
		(%review.getExperience().getId(), user.getId(), review.getRating())
		self.__cursor.execute(query)
		self.__cnx.commit()


	def getAll(self):
		query = "SELECT * from reviews"
		self.__cursor.execute(query)
		reviews_db = self.__cursor.fetchall()
		reviews = []
		for review in reviews_db:
			experience = AdminExperiences.getById(review[0])
			reviews.append(Review(experience, review[2]))
		return reviews
'''
	def getById(self, id_review):
		query = "SELECT * from reviews WHERE id_user =%i and id_exp = %i" %(id_review[0], id_review[1])
		self.__cursor.execute(query)
		review_db = self.__cursor.fetchone()
		review = ''
		if len(review_db) > 0:
			review = Review(review_db[1], review_db[2])
		return user
'''
	def cerrarConexion(self):
		self.__cursor.close()
		self.__cnx.close()