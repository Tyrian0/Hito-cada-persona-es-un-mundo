class MachineLearning:
    def __init__(self, correlations):
        self.__set_correlations()
 
	def train(self, users):
		reviews = {"rating": [], "experience": []}
		for user in users:
			for review in user.getReviews():
				reviews["experience"].append(review.getExperience().getName())
				reviews["rating"].append(review.getRating().getValue())
		corrMatrix = pd.DataFrame(data=reviews).pivot(columns=['experience'],values='rating').corr(method='pearson', min_periods=1)
		self.__setCorrelations(corrMatrix)
