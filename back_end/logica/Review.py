#from Experience import Experience
#from Rating import Rating
from logica.Experience import *
from logica.Rating import *

class ReviewException(Exception):
	pass

class IdNoValidException(ReviewException):
	def __init__(this):
		ReviewException.__init__(this, "id debe ser una tupla de enteros.")

class ExprienceNoValidException(ReviewException):
	def __init__(this):
		ReviewException.__init__(this, "experience debe ser un objeto de la clase Experience.")

class RatingNoValidException(ReviewException):
	def __init__(this):
		ReviewException.__init__(this, "rating debe ser un objeto de la clase Rating")

class Review:
	#Constructor
		#id: opcional, si no se incluye no se crea atributo
	def __init__ (this, experience, rating, id = None):
		if id != None:
			this.setId(id)
		this.__setExperience(experience)
		this.__setRating(rating)

	#Seter de Id
		#Si id no es una tupla de int se lanza una exacepción
	def setId(this, id):
		#Comprobamos que el id sea una tupla de dos elementos
		if id == None or type (id) != type(()) or len(id) != 2:
			raise IdNoValidException()
		#Comprobamos que id contenga enteros
		for sub_id in id:
			if type (sub_id) != int:
				raise IdNoValidException()
		this.__id = id
	def getId(this):
		return this.__id

	#Seter de experience
		#Si experience no es un objeto de la clase Experience se lanza una excepción
	def __setExperience(this, experience):
		if experience == None or type (experience) != Experience:
			raise ExperienceNoValidException()
		this.__experience = experience
	def getExperience(this):
		return this.__experience

	#Seter de rating
		#Si rating no es un objeto de la clase Rating se lanza una excepción
	def __setRating(this, rating):
		if rating == None or type (rating) != Rating:
			raise RatingNoValidException()
		this.__rating = rating
	def getRating(this):
		return this.__rating