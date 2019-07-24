import sys
sys.path.append('../')

import mysql.connector
from logica.Review import *
from logica.Rating import *
from logica.User import *
from logica.Experience import *

class AdminReview:

	def __init__(self):
		self.__cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
		self.__cursor = self.__cnx.cursor(buffered = True)

	def addReview(self, review, user):
		if review == None or type (review) != Review:
			raise ReviewNoValidException()
		if user == None or type (user) != User:
			raise UserNoValidException()
		retrievedReview = self.getReviewFromUserAndExperience(user, review.getExperience())
		if type(retrievedReview) != Review or retrievedReview is None:
			query = "INSERT INTO reviews(id_exp, id_user, rating) VALUES (%i, %i, %f)" \
			%(review.getExperience().getId(), user.getId(), review.getRating().getValue())
			self.__cursor.execute(query)
			self.__cnx.commit()
		else:
			return 'You reviewed this experience before!'

	def getReviewFromUserAndExperience(self, user, experience):
		if user == None or type (user) != User:
			raise UserNoValidException()
		if experience == None or type (experience) != Experience:
			raise ExperienceNoValidException()	
		query = "SELECT r.id_exp, e.name, r.id_user, r.rating FROM reviews r " \
				"JOIN experiences e ON r.id_exp = e.id_exp " \
				"WHERE r.id_user = %i AND r.id_exp = %i" %(user.getId(), experience.getId())
		self.__cursor.execute(query)
		review_db = self.__cursor.fetchone()
		if review_db is None:
			review = None
		else:
			rating = Rating(review_db[3])
			review = Review(experience, rating)
		return review

	def getReviewsFromUser(self, user):
		if user == None or type (user) != User:
			raise UserNoValidException()
		query = "SELECT r.rating, e.name, e.id_exp, t.name, t.id_type from reviews r " \
				"JOIN users u ON u.id_user = r.id_user " \
				"JOIN experiences e ON e.id_exp = r.id_exp " \
				"JOIN types_experiences t ON e.id_type = t.id_type " \
				"WHERE u.id_user = %i" %(user.getId())
		self.__cursor.execute(query)
		reviews_db = self.__cursor.fetchall()
		reviews = []
		for review_db in reviews_db:
			experience = Experience(review_db[1], review_db[3], review_db[2])
			rating = Rating(review_db[0])
			review = Review(experience, rating)
			reviews.append(review)
		return reviews

	def closeConnection(self):
		self.__cursor.close()
		self.__cnx.close()

	def deleteAll(self):
		query = "DELETE FROM reviews"
		self.__cursor.execute(query)
		self.__cnx.commit()

	def deleteReviewsFromUser(self, user):
		query = "DELETE FROM reviews WHERE id_user = %i" %(user.getId())
		self.__cursor.execute(query)
		self.__cnx.commit()

	# def getAll(self):
	# 	query = "SELECT * from reviews"
	# 	self.__cursor.execute(query)
	# 	reviews_db = self.__cursor.fetchall()
	# 	reviews = []
	# 	for review in reviews_db:
	# 		experience = AdminExperience.getById(review[0])
	# 		reviews.append(Review(experience, review[2]))
	# 	return reviews