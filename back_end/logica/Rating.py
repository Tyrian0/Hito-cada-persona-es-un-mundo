class RatingException(Exception):
	pass

class ValueNoValidException(RatingException):
	def __init__(this):
		super ("value debe ser un numero.")

class MinNoValidException(RatingException):
	def __init__(this):
		super ("min debe ser un numero.")

class MaxNoValidException(RatingException):
	def __init__(this):
		super ("max debe ser un numero.")

class OutOfRangeException(RatingException):
	def __init__(this, min, max):
		super ("value not in range [%g,%g)" %(min, max))

class RatingNoValidException(RatingException):
	def __init__(this):
		super ("rating debe ser un objeto de la clase Rating")

class Rating:
	#Definimos el rango de los ratings
	@staticMethod
	def getMinRating:
		return 1.0
	@staticMethod
	def getMinRating:
		return 5.0

	#Constructor
		#min: valor minimo de value, por defecto 1
		#max: valor maximo de value, por defecto 5
			#Si se especifica alguno de los dos se adaptará el numero al rango [1,5)
	def __init__ (this, value, min = getMinRating(), max = getMaxRating()):
		this.setValue(value, min, max)

	#Seter de value
		#Si value no es un numero se lanza una excepción
		#min <= value      . Si no es un numero o no se cumple se lanza una excepción
		#       value < max. Si no es un numero o no se cumple se lanza una excepción
	def setValue(value, min, max)
		if not __isNumber(value):
			raise ValueNoValidException()
		if not __isNumber(min):
			raise MinNoValidException()
		if not __isNumber(max):
			raise MaxNoValidException()
		if min > value or value >= max:
			raise OutOfRangeException(min, max)
		this.__id = id
	def getValue(this):
		return this.__value

	@staticMethod
	def __isNumber(number):
		return number != None and (type (number) == float or type (number) == int)