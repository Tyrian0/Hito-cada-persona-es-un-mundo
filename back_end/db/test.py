import sys
sys.path.append('../')

from AdminUser import *
from AdminTypeExperience import *
from AdminExperience import *
from AdminReview import *
from AdminRecomendation import *
from AdminMachineLearning import *
from logica.User import *
from logica.Experience import *
from logica.Review import *
from logica.Rating import *
from logica.Recomendation import *
from logica.MachineLearning import *

# Adding correlations to DB
adminMachineLearning = AdminMachineLearning()
correlations = adminMachineLearning.getMachineLearning()
machineLearning = MachineLearning(correlations)
#print(correlations)
#adminMachineLearning.calculateCorrelations()
experience1 = Experience('Preambulo Wifi Zone Cafe', 'restaurant', 7885)
experience2 = Experience('Luna Cafe', 'restaurant', 7874)
rating1 = Rating(4)
rating2 = Rating(5)
review1 = Review(experience1, rating1)
review2 = Review(experience2, rating2)
user = User('Igor', '1234', [review1, review2], [], 30958)
machineLearning.recomendate(user)
print(user.getRecomendations())

# experience1 = Experience('Port Aventura', 'Ocio', 1)
# experience2 = Experience('Jamboree', 'Ocio', 2)
# experience3 = Experience('Hotel California', 'hoteles', 3)
# experience4 = Experience('Hotel Alfa', 'hoteles', 4)
# experience5 = Experience('Koh i Noor', 'restaurants', 5)
# rating1 = Rating(1)
# rating2 = Rating(2)
# rating3 = Rating(3)
# rating4 = Rating(4)
# rating5 = Rating(5)
# review1 = Review(experience1, rating1)
# review2 = Review(experience4, rating2)
# review3 = Review(experience2, rating3)
# review4 = Review(experience2, rating4)
# review5 = Review(experience3, rating5)
# review6 = Review(experience4, rating4)
# review7 = Review(experience1, rating3)
# review8 = Review(experience5, rating2)
# review9 = Review(experience4, rating1)
# review10 = Review(experience1, rating2)
# review11 = Review(experience3, rating3)
# review12 = Review(experience5, rating4)
# review13 = Review(experience4, rating5)
# review14 = Review(experience3, rating4)
# review15 = Review(experience1, rating1)

# reviews1 = [review1, review2, review3]
# reviews2 = [review4, review5, review6, review7]
# reviews3 = [review8, review9, review10, review11]
# reviews4 = [review12, review13, review14, review15]

# user1 = User('AAAA', '1111', reviews1, [], 1)
# user2 = User('BBBB', '2222', reviews2, [], 2)
# user3 = User('CCCC', '1111', reviews3, [], 3)
# user4 = User('DDDD', '2222', reviews4, [], 4)
# users = [user1, user2, user3, user4]
# machineLearning.train(users)
# print(machineLearning.getCorrelations())
# machineLearning.trainBis(users)
# print(machineLearning.getCorrelations())
#adminReview = AdminReview()
#adminReview.removeOneTimeUsers()

# Testing AdminUser
# adminUser = AdminUser()
# user1 = adminUser.getByUsername('11melissa')
# user2 = adminUser.getByUsernameAndPassword('0Christy', '1234')
# for review in user2.getReviews():
# 	print(review.getExperience().getName())
# 	print(review.getRating().getValue())
# Testing AdminRecomendation
# adminRecomendation = AdminRecomendation()
# experience = Experience('Hotel Alfa', 'hotels', 2)
# user = User('James', 'dfjiog5075', [], [], 2)
# rating = Rating(3)
# recomendation = Recomendation(experience, rating)
# print(recomendation)

# adminRecomendation.addRecomendation(recomendation, user)

# Testing AdminReview
# adminReview = AdminReview()
# adminExperience = AdminExperience()
# #experience = Experience('Hotel Alfa', 'hotels', 2)
# experience = Experience('Hotel Beta', 'hotels', 25532)
# adminExperience.addExperience(experience)
# rating = Rating(5)
# review = Review(experience, rating)
# user = User('James', 'dfjiog5075', [], [], 2)
# adminReview.addReview(review, user)
# adminReview.getReviewsFromUser(user)

# Testing Admin User
# adminUser = AdminUser()
# user = User('Robb', 'dfjiog5075')
# adminUser.addUser(user)
# users = adminUser.getAll()
# for user in users:
# 	print(user.getName())

# Testing AdminTypeExperience
# adminTypeExperience = AdminTypeExperience()
# adminTypeExperience.addTypeExperience('restaurants')
# adminTypeExperience.addTypeExperience('hotels')
# print(adminTypeExperience.getAll())
# print(adminTypeExperience.getById(2))
# print(adminTypeExperience.getByName('hotels'))

# Testing AdminExperience
# adminExperience = AdminExperience()
# experience = Experience('Koh i Noor', 'restaurants')
# adminExperience.addExperience(experience)
#experience = Experience('Hotel Alfa', 'hotels')
# adminExperience.addExperience(experience)
# experiences = adminExperience.getAll()
# for exp in experiences:
# 	print(exp.getName())
# experience = adminExperience.getById(1)
# print(experience.getName())