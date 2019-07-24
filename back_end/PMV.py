from db.AdminExperience import AdminExperience
from db.AdminUser import AdminUser
from db.AdminMachineLearning import AdminMachineLearning
from logica.Rating import Rating
from logica.Review import Review
from logica.User import User
from logica.Experience import Experience
from logica.MachineLearning import MachineLearning

def inputExperience(experiences):
    while True:
        experiencia_nombre = input ("Introduzca una experiencia: ")
        for experiencia in experiences:
            if experiencia_nombre == experiencia.getName():
                return experiencia
        else:
            print ("Experiencia no válida")
            
def inputRating():
    while True:
        rating = input ("Valora la experiencia (1-5): ")
        if not rating.isdecimal() or float(rating) < Rating.getMin() or float(rating) > Rating.getMax():
            print ("Valoración no válida")        
        else:
            return float(rating)

adminExperiences = AdminExperience()
experiences = adminExperiences.getAll()
tab = 0
for experience in experiences:
    if tab < len(experience.getName()):
        tab = len(experience.getName())
cadena = "%-"+str(tab)+"s"

adminExperiences.closeConnection()

print (cadena %"EXPERIENCIA", "\t%s" %"TIPO")
for experience in experiences:
    if experience.getType() == "restaurant":
        print(cadena %experience.getName(), "\t%s" %experience.getType())


user = User("tester", "password")

experiencia = inputExperience(experiences)
valoracion = inputRating()
user.addReview(Review(experiencia, Rating(valoracion)))
continuar = input ("Desea continuar? (S/N) ")
while continuar == "S" or continuar == "s":
    experiencia = inputExperience(experiences)
    valoracion = inputRating()
    continuar = input ("Desea continuar? (S/N) ")    
    user.addReview(Review(experiencia, Rating(valoracion)))

adminML = AdminMachineLearning()
#adminML.calculateCorrelations()

ml = adminML.getMachineLearning()
ml.recomendate(user)

recomendations = user.getRecomendationsByType("restaurant")
for recomendation in recomendations:
    print (cadena %recomendation.getExperience().getName(), "\t%g" %recomendation.getRating(), "\t%s" %recomendation.getExperience().getType())
            

    

adminML.closeConnection()
            

    
