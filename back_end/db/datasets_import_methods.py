from AdminTypeExperience import *
from AdminExperience import *
from AdminUser import *
from AdminRecomendation import *
from AdminReview import *

# Adding type to database
def addType(type_experience):
	adminTypeExperience = AdminTypeExperience()	
	adminTypeExperience.addTypeExperience(type_experience)

# Adding experiences to database
def addExperiences(ratings, type_experience):
	adminExperience = AdminExperience()
	experiences = ratings.groupby('experience_name').first()
	for experience_name in experiences.index:
		experience = Experience(experience_name, type_experience)
		adminExperience.addExperience(experience)

# Adding users to database
def addUsers(ratings):
	adminUser = AdminUser()
	users = ratings.groupby('user_name').first()
	default_password = '1234'
	for user_name in users.index:
		user = User(user_name, default_password)
		adminUser.addUser(user)

# Adding reviews to database
def addReviews(ratings, min = 1, max = 5):
	adminReview = AdminReview()
	adminExperience = AdminExperience()
	adminUser = AdminUser()
	for index, row in ratings.iterrows():
		experience = adminExperience.getByName(row['experience_name'])
		user = adminUser.getByUsername(row['user_name'])
		rating = Rating(row['rating'], min, max)
		review = Review(experience, rating)
		adminReview.addReview(review, user)