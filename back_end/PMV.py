from db.AdminExperience import AdminExperience
from db.AdminUser import AdminUser
from logica.Rating import Rating
from logica.Review import Review
from logica.User import User

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
    print (cadena %experience.getName(), "\t%s" %experience.getType())
