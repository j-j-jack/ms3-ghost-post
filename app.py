import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
import math
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
    session["page"] = 1
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
                    return redirect(url_for("feed"))
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
            "email": request.form.get("email"),
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
    email = mongo.db.users.find_one(
        {"username": session["user"]})["email"]
    password = mongo.db.users.find_one(
        {"username": session["user"]})["password"]
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]

    if request.method == "POST":
        additional_profile_info = {
            "username": username,
            "email": email,
            "password": password,
            "interest": request.form.get("interest"),
            "profile_picture": request.form.get("profile-picture"),
            "location": request.form.get("location"),
            "about": request.form.get("about"),
            # setting a new profile_complete value to true.
            # when the user logs back in they will go straight to the feed page
            "profile_complete": True
        }
        mongo.db.users.update(
            {"_id": ObjectId(user_id)}, additional_profile_info)
       # code for updating/creating a single field in an already existing entry
       # mongo.db.users.update(
       #     {"_id": ObjectId(user_id)}, {"$set": {"newfield": "abc"}})
       # mongo.db.users.update(
       #     {"_id": ObjectId(user_id)}, {"$set": {"newfield": 42}})
        return redirect(url_for("feed"))

    return render_template("finish-profile.html", username=username)


@app.route("/feed", defaults={"page": 1})
@ app.route("/feed<page>")
def feed(page):
    page = int(page)
    nav_direction = page - session["page"]
    session["page"] = page
    stories = list(mongo.db.stories.find())
    story_count = 0
    for entry in stories:
        story_count += 1
        # number of total pages in feed
    page_count = math.ceil(story_count/5)
    # first_number = page + nav_direction
    if page <= 3:
        first_number = 1
        if page_count > 5:
            last_number = 5
        else:
            last_number = page_count
    else:
        if page_count <= 5:
            first_number = 1
            last_number = page_count
        elif page+2 > page_count:
            first_number = page_count-4
            last_number = page_count
        else:
            first_number = page-2
            last_number = page+2

    return render_template(
        "feed.html", stories=stories, page=page, page_count=page_count, first_number=first_number, last_number=last_number, direction=nav_direction)


@ app.route("/add_story", methods=["GET", "POST"])
def add_story():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if request.method == "POST":
        today = date.today()
        now = today.strftime("%B %d, %Y")
        content = request.form.get("content")
        preview = content[0:50] + "..."
        story = {
            "title": request.form.get("title"),
            "category": request.form.get("category"),
            "story_by": username,
            "favs": 0,
            "location": request.form.get("location"),
            "content": content,
            "preview": preview,
            "date_added": now
        }
        mongo.db.stories.insert_one(story)
        return redirect(url_for("feed"))
    return render_template("add-story.html")


def profile_picture_finder(username):
    picture = mongo.db.users.find_one(
        {"username": username})["profile_picture"]
    return picture


@app.context_processor
def context_processor():
    return dict(profile_picture_finder=profile_picture_finder)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
