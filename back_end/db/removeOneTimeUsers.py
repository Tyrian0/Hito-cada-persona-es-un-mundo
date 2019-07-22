import mysql.connector

from AdminUser import *
from AdminReview import *


cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='cada_persona_es_un_mundo')
cursor = cnx.cursor()

def removeOneTimeUsers():
	adminUser = AdminUser()
	adminReview = AdminReview()
	users = adminUser.getAll()
	print(len(users))
	for user in users:
		reviews = adminReview.getReviewsFromUser(user)
		print(len(reviews))
		if len(reviews) < 2:
			adminReview.deleteReviewsFromUser(user)
			adminUser.deleteUser(user)

removeOneTimeUsers()

cursor.close()
