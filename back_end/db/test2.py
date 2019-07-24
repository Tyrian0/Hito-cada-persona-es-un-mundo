import sys
sys.path.append('../')

from AdminUser import *
from AdminTypeExperience import *
from AdminExperience import *
from AdminReview import *
from AdminRecomendation import *
from AdminMachineLearning import AdminMachineLearning
from logica.User import *
from logica.Experience import *
from logica.Review import *
from logica.Rating import *
from logica.Recomendation import *
from logica.MachineLearning import *

adminExperience = AdminExperience()
username = 'juan'
adminUser = AdminUser()
experience_name = '11th Avenue Hotel Hostel'
rating_value = 2
experience = adminExperience.getByName(experience_name)
print(experience.getId())

rating = Rating(rating_value)
user = adminUser.getByUsername(username)
review = Review(experience, rating)
user.addReview(review)

# for review in user.getReviews():
#     print(review.getExperience().getName())
#     print(review.getExperience().getId())

adminUser.updateUser(user)

adminML = AdminMachineLearning()
correlations = adminML.getMachineLearning()

correlations.recomendate(user)

recomendations = []
for recomendation in user.getRecomendations():
    recomendations.append(recomendation.toJSON())

print(recomendations)