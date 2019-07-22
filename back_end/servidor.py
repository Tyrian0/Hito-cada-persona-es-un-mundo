from flask import Flask, jsonify, request as req
from db.AdminExperience import AdminExperience
from db.AdminUser import AdminUser
from logica.Rating import Rating
from logica.Review import Review
from logica.User import User

app = Flask(__name__) #nuevo objeto

@app.route("/review", methods=["POST"])
def review():
    experience_name = req.form["experience"]
    rating_value = req.form["rating"]

	adminexperience = AdminExperience()
	adminuser = AdminUser()

	experience = adminexperience.getByName(experience_name)
	if experience == None:
		return 420
	if rating_value > Rating.getMax() or rating_value < Rating.getMin():
		return 421

	user = adminuser.getByUsername("tester")
	user.addReview(Review(experience, Rating(rating_value)))

	adminuser.updateUser(user)

	adminesperience.close()
	adminuser.close()

	#Llamamos al método recomend para el PMV
	return recomendate(user)


#@app.route("/recomendate", methods=["POST"])
#def recomendate ():
def recomendate (user):
	adminML = AdminMachineLearning()
	ml = adminML.getMachineLearning()

	ml.recomendate(user)

	recomendations = []
	for recomendation in user.getRecomendations():
		recomendations.append(recomendation.toJSON())

	adminML.close()

	return recomendations

app.run()# se encarga de ejecutar el servidor 5000