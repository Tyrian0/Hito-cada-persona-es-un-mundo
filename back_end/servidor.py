from flask import Flask, session, escape, redirect, url_for, json, jsonify, render_template, request

from db.AdminExperience import AdminExperience
from db.AdminUser import AdminUser
from db.AdminMachineLearning import AdminMachineLearning
from logica.Rating import Rating
from logica.Review import Review
from logica.User import User
from logica.Recomendation import Recomendation

app = Flask(__name__, template_folder='../front_end', static_folder='../front_end') #nuevo objeto

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'the_wheel_of_time'

def login_user(username):
    session['username'] = username
    return redirect(url_for("index"))

@app.route('/', methods=['GET'])
def landing():
    if 'username' in session.keys():
        username = session['username']
        return render_template("landing.html", username=username)
    return render_template("landing.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.getlist('user')[0]
        password = request.form.getlist('password')[0]
        adminUser = AdminUser()
        user = adminUser.getByUsername(username)
        if type(user) == User:
            user = adminUser.getByUsernameAndPassword(username, password)
            if type(user) == User:
                return login_user(username)
            else:
                error = "¡Has introducido una contraseña incorrecta!"
        else:
            error = "¡Este nombre de usuario no existe!"
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    if 'username' in session.keys():
        return redirect(url_for("review")) 
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form.getlist('user')[0]
        password = request.form.getlist('password')[0]
        adminUser = AdminUser()
        user = adminUser.getByUsername(username)
        if type(user) != User:
            user = User(username, password)
            adminUser.addUser(user)
            return login_user(username)
        else:
            error = "¡Este nombre de usuario ya existe!"
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    if 'username' in session.keys():
        return redirect(url_for("review")) 
    return render_template('register.html', error = error)

@app.route('/index')
def index():
    if 'username' not in session.keys():
        return redirect(url_for("login"))
    username = session["username"]
    
    adminUser = AdminUser()
    hasReviews = adminUser.getByUsername(username).hasReviews()
    if hasReviews:
        return redirect(url_for("recomendate"))
    else:
        return redirect(url_for("review"))

@app.route('/logout')
def logout():
    # Elimina el username de session si está ahí
    message = "Has cerrado la sesión correctamente."
    session.pop('username', None)
    return render_template('landing.html', message = message)

@app.route("/review", methods=["GET", "POST"])
def review():
    if 'username' not in session.keys():
        return render_template('landing.html')
    adminExperience = AdminExperience()
    username = session["username"]
    if request.method == 'POST':
        adminUser = AdminUser()
        experience_name = request.form.getlist('experience')[0]
        rating_value = float(request.form.getlist('rating')[0])
        experience = adminExperience.getByName(experience_name)
        rating = Rating(rating_value)
        if experience == None:
            return 420
        # if rating_value > Rating.getMax() or rating_value < Rating.getMin():
        #     return 421

        user = adminUser.getByUsername(username)
        review = Review(experience, rating)
        user.addReview(review)

        adminUser.updateUser(user)

        adminExperience.closeConnection()
        adminUser.closeConnection()

        # Redirigimos a recomendar
        return redirect(url_for("recomendate"))
    else:
        experiences = []
        types = []
        for experience in adminExperience.getAll():
            experiences.append(experience.toJSON())

            type = experience.getType()
            if type not in types:
                types.append(type)
        return render_template('review.html', username=username, experiences = experiences, types = types)

@app.route("/recomendate", methods=["GET"])
def recomendate():
    if 'username' not in session.keys():
        return render_template('landing.html')
    username = session["username"]
    adminUser = AdminUser()
    user = adminUser.getByUsername(username)

    #adminML = AdminMachineLearning()
    #correlations = adminML.getMachineLearning()

    #correlations.recomendate(user)

    recomendations = []
    for recomendation in user.getRecomendations():
        recomendations.append(recomendation.toJSON())

    #adminML.closeConnection()
    adminUser.closeConnection()

    return render_template('recomendacion.html', recomendations = recomendations, username=username)

app.run()# se encarga de ejecutar el servidor 5000