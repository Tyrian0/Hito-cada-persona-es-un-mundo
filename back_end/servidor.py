from flask import Flask, session, escape, redirect, url_for, json, jsonify, render_template, request as req

from db.AdminExperience import AdminExperience
from db.AdminUser import AdminUser
from logica.Rating import Rating
from logica.Review import Review
from logica.User import User

app = Flask(__name__, template_folder='../front_end') #nuevo objeto

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'the_wheel_of_time'

def login_user(username):
    session['username'] = username
    return redirect(url_for("user/'%s'" %(username)))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    adminUser = AdminUser()
    error = None
    user = adminUser.getByUsername(username)
    if type(user) == User:
        user = adminUser.getByUsernameAndPassword(username, password)
        if type(user) == User:
            return login_user(username)
        else:
            error = "Ooops! Wrong password!"
    else:
        error = "This username doesn't exist!"
    return render_template('login.html', error=error)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    adminUser = AdminUser()
    error = None
    user = adminUser.getByUsername(username)
    if type(user) != User:
        adminUser.addUser(username, password)
        return login_user(username)
    else:
        error = "This username already exists!"
    return render_template('register.html', error = error)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/user/<username>')
def index_logged_in(username):
    adminUser = AdminUser()
    user = adminUser.getByUsername(username)
    user_json = json.dumps(user.__dict__)
    if user.getReviews() == 0:
        return render_template("review.html", user = user_json)
    else:
        return render_template("recomendacion.html", user = user_json)

@app.route('/logout')
def logout():
    # Elimina el username de session si está ahí
    message = "Successfully logged out"
    session.pop('username', None)
    return render_template('login.html', message = message)

@app.route("/user/<username>/review", methods=["POST"])
def review(username):
    experience_name = req.form["experience"]
    rating_value = req.form["rating"]
    adminExperience = AdminExperience()
    adminUser = AdminUser()
    experience = adminExperience.getByName(experience_name)
    if experience == None:
        return 420
    if rating_value > Rating.getMax() or rating_value < Rating.getMin():
        return 421

    user = adminUser.getByUsername(username)
    user.addReview(Review(experience, Rating(rating_value)))

    adminUser.updateUser(user)

    adminExperience.closeConnection()
    adminUser.closeConnection()

    # Redirigimos a recomendar
    return redirect(url_for("/user/'%s'/recomendate" %(username)))

@app.route("/user/<username>/recomendate", methods=["POST"])
def recomendate(username):
    adminUser = AdminUser()
    user = adminUser.getByUsername(username)

    adminML = AdminMachineLearning()
    ml = adminML.getMachineLearning()

    ml.recomendate(user)

    recomendations = []
    for recomendation in user.getRecomendations():
        recomendations.append(recomendation.toJSON())

    adminML.close()
    adminUser.close()

    return recomendations

app.run()# se encarga de ejecutar el servidor 5000