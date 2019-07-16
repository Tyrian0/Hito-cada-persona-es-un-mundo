class RatingException(Exception):
	pass

class ValueNoValidException(RatingException):
	def __init__(this):
		RatingException.__init__(this, "value debe ser un numero.")

class MinNoValidException(RatingException):
	def __init__(this):
		RatingException.__init__(this, "min debe ser un numero.")

class MaxNoValidException(RatingException):
	def __init__(this):
		RatingException.__init__(this, "max debe ser un numero.")

class OutOfRangeException(RatingException):
	def __init__(this, min, max):
		RatingException.__init__(this, "value not in range [%g,%g]" %(min, max))

class Rating:
	#Definimos el rango de los ratings como "constantes"
	@staticmethod
	def getMin():
		return 1.0
	@staticmethod
	def getMax():
		return 5.0

	#Constructor
	def __init__ (this, value, min = None, max = None):
		this.__setValue(value, min, max)

	#Definimos los Rating como inmutables
		#min: valor minimo de value, por defecto Rating.getMin()
		#max: valor maximo de value, por defecto Rating.getMax()
		#Se adapta el numero al rango [1,5]
	def __setValue(this, value, min, max):
		if (min == None):
			min = Rating.getMin()
		if (max == None):
			max = Rating.getMax()
		this.__value = Rating.resize(value, min, max)
	def getValue(this):
		return this.__value

	@staticmethod
	def __isNumber(number):
		return number != None and (type (number) == float or type (number) == int)

	#Si value no es un numero se lanza una excepción
		#min <= value      . Si no es un numero o no se cumple se lanza una excepción
		#       value < max. Si no es un numero o no se cumple se lanza una excepción
		#Convierte numeros del rango [min,max] a [Rating.getMin,Rating.getMax]
	@staticmethod
	def resize(value, min, max):
		if not Rating.__isNumber(value):
			raise ValueNoValidException()
		if not Rating.__isNumber(min):
			raise MinNoValidException()
		if not Rating.__isNumber(max):
			raise MaxNoValidException()
		if min > value or value > max:
			raise OutOfRangeException(min, max)
		return (value-min)/(max-min)*(Rating.getMax()-Rating.getMin()) + Rating.getMin()

	def __str__ (this):
		return str(this.getValue())