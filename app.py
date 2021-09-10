import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/login",  methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # if password matches user's password in database
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                # The following if/else checks if the user has finished completing their profile.
                # If they have they are directed to the feed page.
                # Otherwise they are directed to the finish profile page.
                if existing_user["profile_complete"] == False:
                    return redirect(url_for("finish_profile"))
                else:
                    return render_template("feed.html")
            else:
                # login category added to direct message to login form
                flash("Incorrect Username and/or Password", "login")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", "login")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # register category added to direct message to login form
            flash("Username already exists", 'register')
            return redirect(url_for("login"))

        # following code checks if password fields in form match
        password_one = request.form.get("password1")
        password_two = request.form.get("password2")
        if password_one != password_two:
            flash("Passwords do not match", "register")
            return redirect(url_for("login"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password1")),
            # setting a new profile_complete value to false.
            # if user logs back in without finishing profile this value will be checked
            "profile_complete": False
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return redirect(url_for("finish_profile"))


@app.route("/finish_profile", methods=["GET", "POST"])
def finish_profile():
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("finish-profile.html", username=username)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
