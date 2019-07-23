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
    print('hello from login_user!!!!!!!!!!!!!')
    return redirect(url_for("index"))

@app.route('/', methods=['GET'])
def landing():
    return render_template("index.html")

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
                error = "Ooops! Wrong password!"
        else:
            error = "This username doesn't exist!"
    # the code below is executed if the request method
    # was GET or the credentials were invalid
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
            error = "This username already exists!"
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('register.html', error = error)

@app.route('/index')
def index():
    print('hello from index!!!!!!!!')
    username = session["username"]
    adminUser = AdminUser()
    recomendations = adminUser.getByUsername(username).getRecomendations()
    print(recomendations)
    # Object Recomendation is not JSON serializable
    #recomendations_json = json.dumps(recomendations.__dict__)
    recomendations_json = json.dumps([recomendation.__dict__ for recomendation in recomendations])
    print(recomendations_json)
    if len(recomendations) == 0:
        return render_template("review.html", recomendations = recomendations_json)
    else:
        return render_template("recomendacion.html", recomendations = recomendations_json)

@app.route('/logout')
def logout():
    # Elimina el username de session si está ahí
    message = "Successfully logged out"
    session.pop('username', None)
    return render_template('login.html', message = message)

@app.route("/review", methods=["GET", "POST"])
def review():
    adminExperience = AdminExperience()
    if request.method == 'POST':
        username = session["username"]
        adminUser = AdminUser()
        experience_name = req.form["experience"]
        rating_value = req.form["rating"]        
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
        return redirect(url_for("recomendate"))
    else:
        experiences = []
        for experience in adminExperience.getAll():
            experiences.append(experience.toJSON())
        return render_template('review.html', experiences = experiences)

@app.route("/recomendate", methods=["GET"])
def recomendate():
    username = session["username"]
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

    return render_template('recomendacion.html', recomendations = recomendations)

app.run()# se encarga de ejecutar el servidor 5000