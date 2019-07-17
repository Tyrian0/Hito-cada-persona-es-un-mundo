import sys
sys.path.append('../')

from AdminUser import *
from AdminTypeExperience import *
from AdminExperience import *
from AdminReview import *
from logica.User import *
from logica.Experience import *
from logica.Review import *
from logica.Rating import *

# Testing Admin User
# adminUser = AdminUser()
#user = User('James', 'dfjiog5075')
# adminUser.addUser(user1)
# users = adminUser.getAll()
# for user in users:
# 	user_from_getById = adminUser.getById(user)
# 	print(user_from_getById.getId())

# Testing AdminTypeExperience
#adminTypeExperience = AdminTypeExperience()
# adminTypeExperience.addTypeExperience('restaurants')
# adminTypeExperience.addTypeExperience('hotels')
#print(adminTypeExperience.getAll())
#print(adminTypeExperience.getById(2))
#print(adminTypeExperience.getByName('hotels'))

# Testing AdminExperience
#adminExperience = AdminExperience()
#experience = Experience('Koh i Noor', 'restaurants')
#adminExperience.addExperience(experience)
#experience = Experience('Hotel Alfa', 'hotels')
#adminExperience.addExperience(experience)
# experiences = adminExperience.getAll()
# for exp in experiences:
# 	print(exp.getName())
# experience = adminExperience.getById(1)
# print(experience.getName())

# Testing AdminReview
adminReview = AdminReview()
experience = Experience('Hotel Alfa', 'hotels')
print(experience.getName())
rating = Rating(4)
review = Review(experience, rating)
user = User('James', 'dfjiog5075')
adminReview.addReview(review, user)