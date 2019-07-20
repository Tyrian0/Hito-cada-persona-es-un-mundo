import pandas as pd
import numpy as np

from AdminTypeExperience import *
from AdminExperience import *
from AdminUser import *
from AdminRecomendation import *
from AdminReview import *
from delete_data import *
from datasets_import_methods import *

# Clear database (DO NOT USE!!!)
#delete_data()

# Read dataset hotels (csv)
hotel_reviews = pd.read_csv('.\\data\\hotel_reviews.csv', sep=';', usecols=range(3), encoding ='ISO-8859-1')
hotel_reviews = hotel_reviews.dropna()
type_experience = 'hotel'

#addType(type_experience)
#addExperiences(hotel_reviews, type_experience)
#addUsers(hotel_reviews)
addReviews(hotel_reviews)

# Read dataset restaurants (csv)
cols1 = ["userID", "placeID", "rating"]
rating_final = pd.read_csv('.\\data\\restaurant_dataset\\rating_final.csv', usecols = cols1 , sep = ',', encoding ='ISO-8859-1')

cols2 = ["placeID", "name"]
restaurant_data = pd.read_csv('.\\data\\restaurant_dataset\\geoplaces2.csv', usecols = cols2, sep = ',', encoding ='ISO-8859-1')

restaurant_reviews = pd.merge(rating_final, restaurant_data)
del restaurant_reviews['placeID']
restaurant_reviews.columns = ['user_name', 'rating', 'experience_name']
restaurant_reviews = restaurant_reviews.dropna()

type_experience = 'restaurant'

# addType(type_experience)
# addExperiences(restaurant_reviews, type_experience)
# addUsers(restaurant_reviews)
# addReviews(restaurant_reviews)