import sys
sys.path.append('../')

from AdminTypeExperience import *
from AdminExperience import *
from AdminUser import *
from AdminRecomendation import *
from AdminReview import *

# Clear database (NO USAR!!!)
def delete_data():
	adminTypeExperience = AdminTypeExperience()
	adminExperience = AdminExperience()
	adminUser = AdminUser()
	adminRecomendation = AdminRecomendation()
	adminReview = AdminReview()
	adminRecomendation.deleteAll()
	adminReview.deleteAll()
	adminExperience.deleteAll()
	adminUser.deleteAll()
	adminTypeExperience.deleteAll()