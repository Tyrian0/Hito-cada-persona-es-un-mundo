from Rating import Rating
from Experience import Experience
from Review import Review
from User import User
from Recomendation import Recomendation

print (0, "->", Rating (0,0,2))
print (1, "->", Rating (1,0,2))
print (2, "->", Rating (2,0,2))
#Rating(9,0,2)
#Rating("g")
experiencia1 = Experience("Buenas migas", "Restaurante",1)
experiencia2 = Experience("Telepizza", "Restaurante")
experiencia2.setId(2)
valoracion1 = Rating(1)
resenya1 = Review(experiencia1, valoracion1)
recomendacion1 = Recomendation(experiencia2, Rating(2))
user1 = User("nombre", "contraseña")
user1.setId(1)
user1.addRecomendation(Recomendation(Experience("Dominus", "Restaurante",1), Rating(3)))
user1.addReview(Review(Experience("Dominus", "Restaurante",3), Rating(4)))
user1.getRecomendations()[0].setId((user1.getRecomendations()[0].getExperience().getId(),user1.getId()))
user1.getReviews()[0].setId((user1.getReviews()[0].getExperience().getId(),user1.getId()))

user2 = User("otroUser", "otraPassword", id=3)
user2.setRecomendations(user1.getRecomendations())
user3 = User("copion", "copionpassword", user1.getReviews(), user2.getRecomendations(), 3)
