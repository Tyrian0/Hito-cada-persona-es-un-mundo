from logica.Experience import *
from logica.Recomendation import *
from logica.Review import *

class UserException(Exception):
    pass

class UserNoValidException(UserException):
    def __init__(this):
        UserException.__init__(this, "user debe ser un objeto de la clase User.")

class IdNoValidException(UserException):
    def __init__(this):
        UserException ("id debe ser un entero.")

class NameNoValidException(UserException):
    def __init__(this):
        UserException ("name debe ser un str.")

class PasswordNoValidException(UserException):
    def __init__(this):
        UserException ("password debe ser un str.")

class ReviewsNoValidException(UserException):
    def __init__(this):
        UserException ("reviews debe ser una lista de objetos Review.")

class ReviewNoValidException(UserException):
    def __init__(this):
        UserException.__init__(this, "review debe ser una instancia de Review.")

class RecomendationsNoValidException(UserException):
    def __init__(this):
        UserException.__init__(this, "recomendations debe ser una lista de objetos Recomendation.")

class RecomendationsNoValidException(UserException):
    def __init__(this):
        UserException.__init__(this, "recomendation debe ser una instancia de Recomendation.")

class HasNotRecomendationsException(UserException):
    def __init__(this):
        UserException.__init__(this, "El usuario no tiene recomendaciones.")

class HasNotReviewsException(UserException):
    def __init__(this):
        UserException.__init__(this, "El usuario no tiene reviews.")

class User:
    #Numero de recomendaciones que se devuelven con getRecomendations
    @staticmethod
    def getMaxRecomendations():
        return 9 #10

    #Constructor
        #id: opcional, si no se incluye no se crea atributo
        #reviews: opcional, por defecto crea una lista vacía
        #recomendations: opcional, por defecto crea una lista vacía
    def __init__ (this, name, password, reviews = [], recomendations = [], id = None):
        if id != None:
            this.setId(id)
        this.__setName(name)
        this.__setPassword(password)
        this.setReviews(reviews)
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
        if name == None or type (name) != str:
            raise NameNoValidException()
        this.__name = name
    def getName(this):
        return this.__name

    #Seter de password
        #Si password no es un string se lanza una excepción
    def __setPassword(this, password):
        if password == None or type (password) != str:
            raise PasswordNoValidException()
        this.__password = password
    def getPassword(this):
        return this.__password

    #Seter de reviews
        #Si name no es una lista de Reviews se lanza una exepción
    def setReviews(this, reviews):
        #Comprobamos que sea una lista
        if reviews == None or type (reviews) != type([]):
            raise ReviewsNoValidException()
        #Comprobamos que contenga Reviews
        for review in reviews:
            if type(review) != Review:
                raise ReviewsNoValidException()
        this.__reviews = reviews
    def getReviews(this):
        if not this.hasReviews():
            raise HasNotReviewsException ()
        
        return this.__reviews

    #Seter de recomendations
        #Si name no es una lista de Recomendations se lanza una exepción
    def setRecomendations(this, recomendations):
        #Comprobamos que sea una lista
        if recomendations == None or type (recomendations) != type([]):
            raise RecomendationsNoValidException()
        #Comprobamos que contenga Reviews
        for recomendation in recomendations:
            if type(recomendation) != Recomendation:
                raise RecomendationsNoValidException()
        this.__recomendations = recomendations

    #Devuelve las recomendaciones ordenadas por rating.
    def getRecomendations(this):
        if not this.hasRecomendations():
            raise HasNotRecomendationsException()
        recomendations = this.__recomendations
        print ("getRecomendations",len(recomendations))
        return this.filterRecomendations(recomendations)

    def filterRecomendations(this, recomendations):
        for review in this.getReviews():    
            for recomendation in recomendations.copy():
                if recomendation.getExperience() == review.getExperience():
                    recomendations.remove(recomendation)
        print ("filterRecomendations",len(recomendations))
        recomendations.sort(reverse = True, key=lambda x : x.getRating())
        return recomendations[:User.getMaxRecomendations()]

    #Método para añadir una review a la lista.
        #Si review no es un objeto de la clase Review se lanza una excepción.
    def addReview(this, review):
        if review == None or type (review) != Review:
            raise ReviewNoValidException()
        this.__reviews.append(review)

    #Método para añadir una review a la lista.
        #Si review no es un objeto de la clase Review se lanza una excepción.
    def addRecomendation(this, recomendation):
        if recomendation == None or type (recomendation) != Recomendation:
            raise RecomendationNoValidException()
        this.__recomendations.append(recomendation)

    def hasReviews (this):
        return bool(this.__reviews)
    
    def hasRecomendations (this):
        return bool(this.__recomendations)

    def getRecomendationsByType(this, type):
        if not this.hasRecomendations():
            raise HasNotRecomendationsException ()
        recomendations = this.__recomendations
        for recomendation in recomendations.copy():
            if recomendation.getExperience().getType() != type:
                recomendations.remove(recomendation)
        recomendations = this.filterRecomendations(recomendations)        
        return recomendations

