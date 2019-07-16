import pandas as pd

hotels_cols = ['name', 'reviews.rating', 'reviews.username']
ratings = pd.read_csv('.\\data\\hotel_reviews.csv', sep='|', encoding ='ISO-8859-1')

print(ratings)
