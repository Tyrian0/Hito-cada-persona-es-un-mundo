class MachineLearning:
    def __init__(self, correlations):
        self.__setCorrelations(correlations)
 
	def train(self, users):
		reviews = {"rating": [], "experience": []}
		for user in users:
			for review in user.getReviews():
				reviews["experience"].append(review.getExperience().getName())
				reviews["rating"].append(review.getRating().getValue())
		corrMatrix = pd.DataFrame(data=reviews).pivot(columns=['experience'],values='rating').corr(method='pearson', min_periods=1)
		self.__setCorrelations(corrMatrix)

	def recomendate(self, user):
		diccionario = {}
		for experience in self.correlations:
			dicionario.update(experience, 0)
		# Recorremos las reviews del usuario.
		for review in user.getReviews():
			#regresión lineal y = mx + b. 1. Consigo el rating. 2. Set del rating.  	
			for experience,correlation in self.correlations[review.getExperience().getName()].dropna().items():
				diccionario[experience] += correlation*review.getRating()
		recomendations = []
		for experience, rating in diccionario.items():
			recomendations.append(Recomendation(Experience(experience), rating))
		user.setRecomendations(recomendations)



	def __setCorrelations(self, correlations):
		self.correlations = correlations

	def getCorrelations(self):
		return self.correlations






