class UserException(Exception):
	pass

class IdNoValidException(UserException):
	def __init__(this):
		UserException ("id debe ser un entero.")

class NameNoValidException(UserException):
	def __init__(this):
		UserException ("name debe ser una cadena.")

class PasswordNoValidException(UserException):
	def __init__(this):
		UserException ("password debe ser una cadena.")

class ReviewsNoValidException(UserException):
	def __init__(this):
		UserException ("reviews debe ser una lista de objetos Review.")

class ReviewNoValidException(UserException):
	def __init__(this):
		UserException ("review debe ser una instancia de Review.")

class RecomendationsNoValidException(UserException):
	def __init__(this):
		UserException ("recomendations debe ser una lista de objetos Recomendation.")

class RecomendationNoValidException(UserException):
	def __init__(this):
		UserException ("recomendation debe ser una instancia de Recomendation.")

class User:
	#Constructor
		#id: opcional, si no se incluye no se crea atributo
		#reviews: opcional, por defecto crea una lista vacía
		#recomendations: opcional, por defecto crea una lista vacía
	def __init__ (this, id = None, name, password, reviews = [], recomendations = []):
		if id != None:
			this.setId(id)
		this.__setName(name)
		this.__setPassword(password)
		this.__setReviews(reviews)
		this.setRecomendations(recomendations)

	#Seter de Id
		#Si id no es un int se lanza una exacepción
	def setId(this, id):
		if id == None or type (id) != int:
			raise IdNoValidException()
		this.__id = id
	def getId(this):
		return this.__id

	#Seter de name
		#Si name no es un string se lanza una excepción
	def __setName(this, name):
		if name == None or type (name) != string:
			raise NameNoValidException()
		this.__name = name
	def getName(this):
		return this.__name

	#Seter de password
		#Si password no es un string se lanza una excepción
	def __setPassword(this, password):
		if name == None or type (name) != string:
			raise PasswordNoValidException()
		this.__password = password
	def getPassword(this):
		return this.__password

	#Seter de reviews
		#Si name no es una lista de Reviews se lanza una exepción
	def __setReviews(this, reviews):
		#Comprobamos que sea una lista
		if reviews == None or type (reviews) != type[]:
			raise ReviewsNoValidException()
		#Comprobamos que contenga Reviews
		for review in reviews:
			if type(review) != Review:
			raise ReviewsNoValidException()
		this.__reviews = reviews
	def getReviews(this):
		return this.__reviews

	#Seter de recomendations
		#Si name no es una lista de Recomendations se lanza una exepción
	def __setRecomendations(this, recomendations):
		#Comprobamos que sea una lista
		if recomendations == None or type (recomendations) != type[]:
			raise RecomendationsNoValidException()
		#Comprobamos que contenga Reviews
		for recomendation in recomendations:
			if type(recomendation) != Recomendation:
			raise RecomendationsNoValidException()
		this.__recomendations = recomendations
	def getRecomendations(this):
		return this.__recomendations

	#Método para añadir una review a la lista.
		#Si review no es un objeto de la clase Review se lanza una excepción.
	def addReview(this, review):
		if review == None or type (review) != Review:
			raise ReviewNoValidException()
		this.__reviews.append(review)

	#Método para añadir una review a la lista.
		#Si review no es un objeto de la clase Review se lanza una excepción.
	def addRecomendation(this, review):
		if recomendation == None or type (recomendation) != Recomendation:
			raise RecomendationNoValidException()
		this.__recomendations.append(recomendation)