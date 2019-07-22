from flask import Flask, jsonify, request as req
import AdminExperience, AdminUser
import Rating, Review, User

app = Flask(__name__) #nuevo objeto

@app.route("/review", methods=["POST"])
def review():
    experience_name = req.form["experience"]
    rating_value = req.form["rating"]

	adminexperience = AdminExperience()
	experience = adminexperience.getByName(experience_name)
	if experience == None:
		return 404

	if rating_value > Rating.getMax() or rating_value < Rating.getMin():
		return 404

	rating = Rating(rating_value)

	review = Review(experience, rating)

	adminuser = AdminUser()

	user_name = adminuser.getByUsername("tester")

	user = User()

	user.addReview(review)

    return jsonify({"about": "¡Hola " + nombre + " " + apellido + "!"})


app.run()# se encarga de ejecutar el servidor 5000