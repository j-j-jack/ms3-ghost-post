import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
import math
import random
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():

    session["flash"] = ""
    session["search"] = ""
    session["user"] = ""
    if request.method == "POST":
        if request.form.get("log_method") == 'logout':
            session.clear()
            flash("You have successfully logged out", "logout")
            return redirect(url_for("login"))
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        if existing_user:
            # if password matches user's password in database
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username")
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
    else:
        session["flash"] = ""
    flash(session["flash"])
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

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
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password1")),
            "email": request.form.get("email"),
            # setting a new profile_complete value to false.
            # if user logs back in without finishing profile this value will be checked
            "profile_complete": False,
            "followers": [],
            "following": [],
            "favorite_stories": []
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username")
        flash("Registration Successful!")
    return redirect(url_for("finish_profile"))


@app.route("/followers", defaults={"username": 1, "page": 1})
@app.route("/followers/<username>/<page>")
def followers(username, page):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    page = int(page)
    if username == 1:
        username = session['user']
    else:
        username = username

    followers = mongo.db.users.find_one(
        {"username": username})["followers"]
    page_count = len(followers)
    page_count = math.ceil(page_count/40)

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

    return render_template('followers.html', username=username, followers=followers,
                           page=page, page_count=page_count, first_number=first_number,
                           last_number=last_number)


@app.route("/following", defaults={"username": 1, "page": 1})
@app.route("/following<username>/<page>")
def following(username, page):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    page = int(page)
    if username == 1:
        username = session['user']
    else:
        username = username

    following = mongo.db.users.find_one(
        {"username": username})["following"]
    page_count = len(following)
    page_count = math.ceil(page_count/40)

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

    return render_template('following.html', username=username, following=following,
                           page=page, page_count=page_count, first_number=first_number,
                           last_number=last_number)


@ app.route("/finish_profile", methods=["GET", "POST"])
def finish_profile():
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    email = mongo.db.users.find_one(
        {"username": session["user"]})["email"]
    password = mongo.db.users.find_one(
        {"username": session["user"]})["password"]
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    followers = mongo.db.users.find_one(
        {"username": session["user"]})["followers"]
    following = mongo.db.users.find_one(
        {"username": session["user"]})["followers"]
    favorite_stories = mongo.db.users.find_one(
        {"username": session["user"]})["favorite_stories"]

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
            "profile_complete": True,
            "favorite_stories": favorite_stories,
            "following": following,
            "followers": followers
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


@ app.route("/feed", defaults={"page": 1, "unfiltered": 0})
@ app.route("/feed/<page>/<unfiltered>")
def feed(page, unfiltered):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    username = session["user"]
    page = int(page)
    unfiltered = int(unfiltered)
    if unfiltered == 0:
        all = "all"
        session["all"] = 'all'
        session["aliens"] = 'Aliens'
        session["angels"] = 'Angels'
        session["demons"] = 'Demons'
        session["fairies"] = 'Fairies'
        session["ghosts"] = 'Ghosts'
        session["vampires"] = 'Vampires'
        session["other"] = "Other"
        session["sort_method"] = 3
        sort_method = 3
    elif unfiltered == 1:
        all = request.args.get('all')
        aliens = request.args.get('aliens')
        angels = request.args.get('angels')
        demons = request.args.get('demons')
        fairies = request.args.get('fairies')
        ghosts = request.args.get('ghosts')
        vampires = request.args.get('vampires')
        witches_wizards = request.args.get('witches_wizards')
        other = request.args.get('other')
        session["all"] = request.args.get('all')
        session["aliens"] = request.args.get('aliens')
        session["angels"] = request.args.get('angels')
        session["demons"] = request.args.get('demons')
        session["fairies"] = request.args.get('fairies')
        session["ghosts"] = request.args.get('ghosts')
        session["vampires"] = request.args.get('vampires')
        session["witches_wizards"] = request.args.get('witches_wizards')
        session['other'] = request.args.get('other')
        session["sort_method"] = int(request.args.get('sort_method'))
        sort_method = int(request.args.get('sort_method'))
    elif unfiltered == 2:
        all = session["all"]
        aliens = session['aliens']
        angels = session['angels']
        demons = session['demons']
        fairies = session['fairies']
        ghosts = session['ghosts']
        vampires = session['vampires']
        witches_wizards = session['witches_wizards']
        other = session['other']
        sort_method = session['sort_method']

    stories = list(mongo.db.stories.find())
    if sort_method == 3:
        stories.reverse()
        oldest_selected = ""
        newest_selected = "selected"
        most_favorites_selected = ""
    elif sort_method == 1:
        stories = sorted(stories, key=lambda i: i['favs'], reverse=True)
        oldest_selected = ""
        newest_selected = ""
        most_favorites_selected = "selected"
    else:
        oldest_selected = "selected"
        newest_selected = ""
        most_favorites_selected = ""

    filtered_stories = []
    if all == "all":
        aliens = "Aliens"
        angels = "Angels"
        demons = "Demons"
        fairies = "Fairies"
        ghosts = "Ghosts"
        vampires = "Vampires"
        witches_wizards = "Witches/Wizards"
        other = "Other"

    for story in stories:
        if story["category"] == aliens:
            filtered_stories.append(story)
        elif story["category"] == angels:
            filtered_stories.append(story)
        elif story["category"] == demons:
            filtered_stories.append(story)
        elif story["category"] == fairies:
            filtered_stories.append(story)
        elif story["category"] == ghosts:
            filtered_stories.append(story)
        elif story["category"] == vampires:
            filtered_stories.append(story)
        elif story["category"] == witches_wizards:
            filtered_stories.append(story)
        elif story["category"] == other:
            filtered_stories.append(story)

    if all == 'all':
        all_checked = "checked"
    else:
        all_checked = "unchecked"

    if aliens == 'Aliens':
        aliens_checked = "checked"
    else:
        aliens_checked = "unchecked"

    if angels == 'Angels':
        angels_checked = "checked"
    else:
        angels_checked = "unchecked"

    if demons == 'Demons':
        demons_checked = "checked"
    else:
        demons_checked = "unchecked"

    if fairies == 'Fairies':
        fairies_checked = "checked"
    else:
        fairies_checked = "unchecked"

    if ghosts == 'Ghosts':
        ghosts_checked = "checked"
    else:
        ghosts_checked = "unchecked"

    if vampires == 'Vampires':
        vampires_checked = "checked"
    else:
        vampires_checked = "unchecked"

    if witches_wizards == 'Witches/Wizards':
        witches_wizards_checked = "checked"
    else:
        witches_wizards_checked = "unchecked"

    if other == 'Other':
        other_checked = "checked"
    else:
        other_checked = "unchecked"

    stories = filtered_stories
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

    flash(session["flash"])
    session["flash"] = ""

    return render_template(
        "feed.html", username=username, stories=stories, page=page,
        page_count=page_count, first_number=first_number,
        last_number=last_number, unfiltered=unfiltered,
        all_checked=all_checked, aliens_checked=aliens_checked,
        angels_checked=angels_checked, demons_checked=demons_checked,
        fairies_checked=fairies_checked, ghosts_checked=ghosts_checked,
        vampires_checked=vampires_checked, witches_wizards_checked=witches_wizards_checked,
        other_checked=other_checked, sort_method=sort_method,
        newest_selected=newest_selected, oldest_selected=oldest_selected,
        most_favorites_selected=most_favorites_selected)


@app.route("/user_stories", defaults={"page": 1, "unfiltered": 0})
@ app.route("/user_stories/<page>/<unfiltered>/<stories_by>")
def user_stories(page, unfiltered, stories_by):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    stories_by = stories_by
    username = stories_by
    page = int(page)
    unfiltered = int(unfiltered)
    if unfiltered == 0:
        all = "all"
        session["all"] = 'all'
        session["aliens"] = 'Aliens'
        session["angels"] = 'Angels'
        session["demons"] = 'Demons'
        session["fairies"] = 'Fairies'
        session["ghosts"] = 'Ghosts'
        session["vampires"] = 'Vampires'
        session["other"] = "Other"
        session["sort_method"] = 3
        sort_method = 3
    elif unfiltered == 1:
        all = request.args.get('all')
        aliens = request.args.get('aliens')
        angels = request.args.get('angels')
        demons = request.args.get('demons')
        fairies = request.args.get('fairies')
        ghosts = request.args.get('ghosts')
        vampires = request.args.get('vampires')
        witches_wizards = request.args.get('witches_wizards')
        other = request.args.get('other')
        session["all"] = request.args.get('all')
        session["aliens"] = request.args.get('aliens')
        session["angels"] = request.args.get('angels')
        session["demons"] = request.args.get('demons')
        session["fairies"] = request.args.get('fairies')
        session["ghosts"] = request.args.get('ghosts')
        session["vampires"] = request.args.get('vampires')
        session["witches_wizards"] = request.args.get('witches_wizards')
        session['other'] = request.args.get('other')
        session["sort_method"] = int(request.args.get('sort_method'))
        sort_method = int(request.args.get('sort_method'))
    elif unfiltered == 2:
        all = session["all"]
        aliens = session['aliens']
        angels = session['angels']
        demons = session['demons']
        fairies = session['fairies']
        ghosts = session['ghosts']
        vampires = session['vampires']
        witches_wizards = session['witches_wizards']
        other = session['other']
        sort_method = session['sort_method']

    all_stories = list(mongo.db.stories.find())
    stories = []
    for story in all_stories:
        if story["story_by"] == username:
            stories.append(story)

    if sort_method == 3:
        stories.reverse()
        oldest_selected = "selected"
        newest_selected = ""
        most_favorites_selected = ""
    elif sort_method == 1:
        stories = sorted(stories, key=lambda i: i['favs'], reverse=True)
        oldest_selected = ""
        newest_selected = ""
        most_favorites_selected = "selected"
    else:
        oldest_selected = ""
        newest_selected = "selected"
        most_favorites_selected = ""

    filtered_stories = []
    if all == "all":
        aliens = "Aliens"
        angels = "Angels"
        demons = "Demons"
        fairies = "Fairies"
        ghosts = "Ghosts"
        vampires = "Vampires"
        witches_wizards = "Witches/Wizards"
        other = "Other"

    for story in stories:
        if story["category"] == aliens:
            filtered_stories.append(story)
        elif story["category"] == angels:
            filtered_stories.append(story)
        elif story["category"] == demons:
            filtered_stories.append(story)
        elif story["category"] == fairies:
            filtered_stories.append(story)
        elif story["category"] == ghosts:
            filtered_stories.append(story)
        elif story["category"] == vampires:
            filtered_stories.append(story)
        elif story["category"] == witches_wizards:
            filtered_stories.append(story)
        elif story["category"] == other:
            filtered_stories.append(story)

    if all == 'all':
        all_checked = "checked"
    else:
        all_checked = "unchecked"

    if aliens == 'Aliens':
        aliens_checked = "checked"
    else:
        aliens_checked = "unchecked"

    if angels == 'Angels':
        angels_checked = "checked"
    else:
        angels_checked = "unchecked"

    if demons == 'Demons':
        demons_checked = "checked"
    else:
        demons_checked = "unchecked"

    if fairies == 'Fairies':
        fairies_checked = "checked"
    else:
        fairies_checked = "unchecked"

    if ghosts == 'Ghosts':
        ghosts_checked = "checked"
    else:
        ghosts_checked = "unchecked"

    if vampires == 'Vampires':
        vampires_checked = "checked"
    else:
        vampires_checked = "unchecked"

    if witches_wizards == 'Witches/Wizards':
        witches_wizards_checked = "checked"
    else:
        witches_wizards_checked = "unchecked"

    if other == 'Other':
        other_checked = "checked"
    else:
        other_checked = "unchecked"

    stories = filtered_stories
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
        "user-stories.html", username=username, stories=stories, page=page,
        page_count=page_count, first_number=first_number,
        last_number=last_number, unfiltered=unfiltered,
        all_checked=all_checked, aliens_checked=aliens_checked,
        angels_checked=angels_checked, demons_checked=demons_checked,
        fairies_checked=fairies_checked, ghosts_checked=ghosts_checked,
        vampires_checked=vampires_checked, witches_wizards_checked=witches_wizards_checked,
        other_checked=other_checked, sort_method=sort_method,
        newest_selected=newest_selected, oldest_selected=oldest_selected,
        most_favorites_selected=most_favorites_selected, stories_by=stories_by)


@app.route("/favorites", defaults={"page": 1, "unfiltered": 0})
@ app.route("/favorites/<page>/<unfiltered>/<favorites_of>")
def favorites(page, unfiltered, favorites_of):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    favorites_of = favorites_of
    username = favorites_of
    page = int(page)
    unfiltered = int(unfiltered)
    if unfiltered == 0:
        all = "all"
        session["all"] = 'all'
        session["aliens"] = 'Aliens'
        session["angels"] = 'Angels'
        session["demons"] = 'Demons'
        session["fairies"] = 'Fairies'
        session["ghosts"] = 'Ghosts'
        session["vampires"] = 'Vampires'
        session["other"] = "Other"
        session["sort_method"] = 3
        sort_method = 3
    elif unfiltered == 1:
        all = request.args.get('all')
        aliens = request.args.get('aliens')
        angels = request.args.get('angels')
        demons = request.args.get('demons')
        fairies = request.args.get('fairies')
        ghosts = request.args.get('ghosts')
        vampires = request.args.get('vampires')
        witches_wizards = request.args.get('witches_wizards')
        other = request.args.get('other')
        session["all"] = request.args.get('all')
        session["aliens"] = request.args.get('aliens')
        session["angels"] = request.args.get('angels')
        session["demons"] = request.args.get('demons')
        session["fairies"] = request.args.get('fairies')
        session["ghosts"] = request.args.get('ghosts')
        session["vampires"] = request.args.get('vampires')
        session["witches_wizards"] = request.args.get('witches_wizards')
        session['other'] = request.args.get('other')
        session["sort_method"] = int(request.args.get('sort_method'))
        sort_method = int(request.args.get('sort_method'))
    elif unfiltered == 2:
        all = session["all"]
        aliens = session['aliens']
        angels = session['angels']
        demons = session['demons']
        fairies = session['fairies']
        ghosts = session['ghosts']
        vampires = session['vampires']
        witches_wizards = session['witches_wizards']
        other = session['other']
        sort_method = session['sort_method']

    all_stories = list(mongo.db.stories.find())
    user_favorites = mongo.db.users.find_one(
        {"username": favorites_of})["favorite_stories"]
    stories = []

    for favorite in user_favorites:
        stories.append(mongo.db.stories.find_one(
            {"_id": ObjectId(favorite)}))

    if sort_method == 3:
        stories.reverse()
        oldest_selected = ""
        newest_selected = "selected"
        most_favorites_selected = ""
    elif sort_method == 1:
        stories = sorted(stories, key=lambda i: i['favs'], reverse=True)
        oldest_selected = ""
        newest_selected = ""
        most_favorites_selected = "selected"
    else:
        oldest_selected = "selected"
        newest_selected = ""
        most_favorites_selected = ""

    filtered_stories = []
    if all == "all":
        aliens = "Aliens"
        angels = "Angels"
        demons = "Demons"
        fairies = "Fairies"
        ghosts = "Ghosts"
        vampires = "Vampires"
        witches_wizards = "Witches/Wizards"
        other = "Other"

    for story in stories:
        if story["category"] == aliens:
            filtered_stories.append(story)
        elif story["category"] == angels:
            filtered_stories.append(story)
        elif story["category"] == demons:
            filtered_stories.append(story)
        elif story["category"] == fairies:
            filtered_stories.append(story)
        elif story["category"] == ghosts:
            filtered_stories.append(story)
        elif story["category"] == vampires:
            filtered_stories.append(story)
        elif story["category"] == witches_wizards:
            filtered_stories.append(story)
        elif story["category"] == other:
            filtered_stories.append(story)

    if all == 'all':
        all_checked = "checked"
    else:
        all_checked = "unchecked"

    if aliens == 'Aliens':
        aliens_checked = "checked"
    else:
        aliens_checked = "unchecked"

    if angels == 'Angels':
        angels_checked = "checked"
    else:
        angels_checked = "unchecked"

    if demons == 'Demons':
        demons_checked = "checked"
    else:
        demons_checked = "unchecked"

    if fairies == 'Fairies':
        fairies_checked = "checked"
    else:
        fairies_checked = "unchecked"

    if ghosts == 'Ghosts':
        ghosts_checked = "checked"
    else:
        ghosts_checked = "unchecked"

    if vampires == 'Vampires':
        vampires_checked = "checked"
    else:
        vampires_checked = "unchecked"

    if witches_wizards == 'Witches/Wizards':
        witches_wizards_checked = "checked"
    else:
        witches_wizards_checked = "unchecked"

    if other == 'Other':
        other_checked = "checked"
    else:
        other_checked = "unchecked"

    stories = filtered_stories
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
        "favorites.html", username=username, stories=stories, page=page,
        page_count=page_count, first_number=first_number,
        last_number=last_number, unfiltered=unfiltered,
        all_checked=all_checked, aliens_checked=aliens_checked,
        angels_checked=angels_checked, demons_checked=demons_checked,
        fairies_checked=fairies_checked, ghosts_checked=ghosts_checked,
        vampires_checked=vampires_checked, witches_wizards_checked=witches_wizards_checked,
        other_checked=other_checked, sort_method=sort_method,
        newest_selected=newest_selected, oldest_selected=oldest_selected,
        most_favorites_selected=most_favorites_selected, favorites_of=favorites_of)


@app.route("/search", defaults={"page": 1, "unfiltered": 0}, methods=["GET", "POST"])
@ app.route("/search/<page>/<unfiltered>")
def search(page, unfiltered):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    if request.method == "POST":
        query = request.form.get("search")
        session["search"] = query
    else:
        query = session["search"]

    username = session["user"]
    page = int(page)
    unfiltered = int(unfiltered)
    if unfiltered == 0:
        all = "all"
        session["all"] = 'all'
        session["aliens"] = 'Aliens'
        session["angels"] = 'Angels'
        session["demons"] = 'Demons'
        session["fairies"] = 'Fairies'
        session["ghosts"] = 'Ghosts'
        session["vampires"] = 'Vampires'
        session["other"] = "Other"
        session["sort_method"] = 2
        sort_method = 2
    elif unfiltered == 1:
        all = request.args.get('all')
        aliens = request.args.get('aliens')
        angels = request.args.get('angels')
        demons = request.args.get('demons')
        fairies = request.args.get('fairies')
        ghosts = request.args.get('ghosts')
        vampires = request.args.get('vampires')
        witches_wizards = request.args.get('witches_wizards')
        other = request.args.get('other')
        session["all"] = request.args.get('all')
        session["aliens"] = request.args.get('aliens')
        session["angels"] = request.args.get('angels')
        session["demons"] = request.args.get('demons')
        session["fairies"] = request.args.get('fairies')
        session["ghosts"] = request.args.get('ghosts')
        session["vampires"] = request.args.get('vampires')
        session["witches_wizards"] = request.args.get('witches_wizards')
        session['other'] = request.args.get('other')
        session["sort_method"] = int(request.args.get('sort_method'))
        sort_method = int(request.args.get('sort_method'))
    elif unfiltered == 2:
        all = session["all"]
        aliens = session['aliens']
        angels = session['angels']
        demons = session['demons']
        fairies = session['fairies']
        ghosts = session['ghosts']
        vampires = session['vampires']
        witches_wizards = session['witches_wizards']
        other = session['other']
        sort_method = session['sort_method']

    stories = list(mongo.db.stories.find({"$text": {"$search": query}}))
    if sort_method == 3:
        stories.reverse()
        oldest_selected = ""
        newest_selected = "selected"
        most_favorites_selected = ""
    elif sort_method == 1:
        stories = sorted(stories, key=lambda i: i['favs'], reverse=True)
        oldest_selected = ""
        newest_selected = ""
        most_favorites_selected = "selected"
    else:
        oldest_selected = "selected"
        newest_selected = ""
        most_favorites_selected = ""

    filtered_stories = []
    if all == "all":
        aliens = "Aliens"
        angels = "Angels"
        demons = "Demons"
        fairies = "Fairies"
        ghosts = "Ghosts"
        vampires = "Vampires"
        witches_wizards = "Witches/Wizards"
        other = "Other"

    for story in stories:
        if story["category"] == aliens:
            filtered_stories.append(story)
        elif story["category"] == angels:
            filtered_stories.append(story)
        elif story["category"] == demons:
            filtered_stories.append(story)
        elif story["category"] == fairies:
            filtered_stories.append(story)
        elif story["category"] == ghosts:
            filtered_stories.append(story)
        elif story["category"] == vampires:
            filtered_stories.append(story)
        elif story["category"] == witches_wizards:
            filtered_stories.append(story)
        elif story["category"] == other:
            filtered_stories.append(story)

    if all == 'all':
        all_checked = "checked"
    else:
        all_checked = "unchecked"

    if aliens == 'Aliens':
        aliens_checked = "checked"
    else:
        aliens_checked = "unchecked"

    if angels == 'Angels':
        angels_checked = "checked"
    else:
        angels_checked = "unchecked"

    if demons == 'Demons':
        demons_checked = "checked"
    else:
        demons_checked = "unchecked"

    if fairies == 'Fairies':
        fairies_checked = "checked"
    else:
        fairies_checked = "unchecked"

    if ghosts == 'Ghosts':
        ghosts_checked = "checked"
    else:
        ghosts_checked = "unchecked"

    if vampires == 'Vampires':
        vampires_checked = "checked"
    else:
        vampires_checked = "unchecked"

    if witches_wizards == 'Witches/Wizards':
        witches_wizards_checked = "checked"
    else:
        witches_wizards_checked = "unchecked"

    if other == 'Other':
        other_checked = "checked"
    else:
        other_checked = "unchecked"

    stories = filtered_stories
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
    if stories == []:
        flash("No results found. Adjust your query and try again", "search")
    return render_template(
        "search.html", username=username, stories=stories, page=page,
        page_count=page_count, first_number=first_number,
        last_number=last_number, unfiltered=unfiltered,
        all_checked=all_checked, aliens_checked=aliens_checked,
        angels_checked=angels_checked, demons_checked=demons_checked,
        fairies_checked=fairies_checked, ghosts_checked=ghosts_checked,
        vampires_checked=vampires_checked, witches_wizards_checked=witches_wizards_checked,
        other_checked=other_checked, sort_method=sort_method,
        newest_selected=newest_selected, oldest_selected=oldest_selected,
        most_favorites_selected=most_favorites_selected, query=query)


@ app.route("/add_story", methods=["GET", "POST"])
def add_story():
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
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
        session["flash"] = "Story added!"
        return redirect(url_for("feed"))
    return render_template("add-story.html")


@ app.route("/profile", defaults={"username": "site_user"})
@ app.route("/profile/<username>")
def profile(username):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    username = username
    own_profile = 'no'
    if username == "site_user":
        username = session['user']
        own_profile = 'yes'
    if session["user"] == username:
        own_profile = 'yes'
    following = mongo.db.users.find_one(
        {"username": session["user"]})["following"]
    follows = 'no'
    if username in following:
        follows = 'yes'
    else:
        follows = 'no'
    username = mongo.db.users.find_one(
        {"username": username})["username"]
    profile_picture = mongo.db.users.find_one(
        {"username": username})["profile_picture"]
    location = mongo.db.users.find_one(
        {"username": username})["location"]
    interest = mongo.db.users.find_one(
        {"username": username})["interest"]
    about = mongo.db.users.find_one(
        {"username": username})["about"]

    flash(session["flash"])
    session["flash"] = ""
    return render_template("profile.html", username=username,
                           profile_picture=profile_picture,
                           location=location, interest=interest, about=about,
                           own_profile=own_profile, follows=follows)


@ app.route("/follow_user/<username>")
def follow_user(username):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    username = username
    following = mongo.db.users.find_one(
        {"username": session["user"]})["following"]
    following.append(username)
    following.sort()
    session["flash"] = "You are now following " + username
    mongo.db.users.update(
        {"username": session["user"]}, {"$set": {"following": following}})
    return redirect(url_for("profile", username=username))


@ app.route("/unfollow_user/<username>")
def unfollow_user(username):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    username = username
    following = mongo.db.users.find_one(
        {"username": session["user"]})["following"]
    following.remove(username)
    following.sort()
    session["flash"] = "You are no longer following " + username
    mongo.db.users.update(
        {"username": session["user"]}, {"$set": {"following": following}})
    return redirect(url_for("profile", username=username))


@ app.route("/edit_story/<story>", methods=["GET", "POST"])
def edit_story(story):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    story = story
    username = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["story_by"]
    # prevent non-authorised user from editing a story that isn't theirs
    if session['user'] != username:
        session["flash"] = "Oops, you don't have permission for that!"
        return redirect(url_for("feed"))
    if request.method == "POST":
        new_content = request.form.get("content")
        preview = new_content[0:50] + "..."
        mongo.db.stories.update(
            {"_id": ObjectId(story)}, {"$set": {"title": request.form.get("title")}})
        mongo.db.stories.update(
            {"_id": ObjectId(story)}, {"$set": {"location": request.form.get("location")}})
        mongo.db.stories.update(
            {"_id": ObjectId(story)}, {"$set": {"category": request.form.get("category")}})
        mongo.db.stories.update(
            {"_id": ObjectId(story)}, {"$set": {"content": request.form.get("content")}})
        mongo.db.stories.update(
            {"_id": ObjectId(story)}, {"$set": {"preview": preview}})
        session["flash"] = "Story edited!"
        return redirect(url_for("feed"))
    title = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["title"]
    category = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["category"]
    location = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["location"]
    content = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["content"]

    return render_template("edit-story.html", title=title, category=category, location=location,
                           content=content, username=username, story=story)


@ app.route("/delete_story/<story>")
def delete_story(story):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    mongo.db.stories.remove(
        {"_id": ObjectId(story)})
    session["flash"] = "Story deleted"
    return redirect(url_for("feed"))


def remove_follower(user_to_remove):
    site_user = session["user"]
    site_user_following = mongo.db.users.find_one(
        {"username": site_user})["following"]
    site_user_following.remove(user_to_remove)
    mongo.db.users.update(
        {"username": site_user}, {"$set": {"following": site_user_following}})


@ app.route("/view_story/<story>", methods=["GET", "POST"])
def view_story(story):
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    favorite_stories = mongo.db.users.find_one(
        {"username": session["user"]})["favorite_stories"]
    favorites_count = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["favs"]
    if request.method == "POST":
        story_to_add_or_remove = story

        if story in favorite_stories:
            favorite_stories.remove(story_to_add_or_remove)
            mongo.db.users.update(
                {"username": session["user"]}, {"$set": {"favorite_stories": favorite_stories}})
            favorites_count = favorites_count-1
            mongo.db.stories.update(
                {"_id": ObjectId(story)}, {"$set": {"favs": favorites_count}})
            flash("Story removed from favorites")
        else:
            favorite_stories.append(story_to_add_or_remove)
            mongo.db.users.update(
                {"username": session["user"]}, {"$set": {"favorite_stories": favorite_stories}})
            favorites_count = favorites_count+1
            mongo.db.stories.update(
                {"_id": ObjectId(story)}, {"$set": {"favs": favorites_count}})
            flash("Story added to favorites")

    favorited = ""
    if story in favorite_stories:
        favorited = "In Favorites"
    else:
        favorited = "Not in Favorites"

    title = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["title"]
    category = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["category"]
    location = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["location"]
    content = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["content"]
    favs = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["favs"]
    story_by = mongo.db.stories.find_one(
        {"_id": ObjectId(story)})["story_by"]

    if story_by == session['user']:
        owns_story = 'yes'
    else:
        owns_story = 'no'
    user_favorites = mongo.db.users.find_one(
        {"username": session["user"]})["favorite_stories"]

    return render_template('story.html', title=title, category=category, location=location,
                           content=content, favs=favs, story_by=story_by, owns_story=owns_story, id=story,
                           user_favorites=user_favorites, favorited=favorited)


@ app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    logged_in = logged_in_test()
    if logged_in == False:
        return render_template("not-logged-in.html")
    # it is impossible to edit someone else's profile by url.
    # the edit profile link can only bring a user to edit their own profile
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    email = mongo.db.users.find_one(
        {"username": session["user"]})["email"]
    location = mongo.db.users.find_one(
        {"username": session["user"]})["location"]
    about = mongo.db.users.find_one(
        {"username": session["user"]})["about"]
    interest = mongo.db.users.find_one(
        {"username": session["user"]})["interest"]
    profile_picture = mongo.db.users.find_one(
        {"username": session["user"]})["profile_picture"]
    profile_picture = profile_picture[::-1]
    profile_picture = profile_picture[4]

    if request.method == "POST":
        mongo.db.users.update(
            {"username": username}, {"$set": {"email": request.form.get("email")}})
        mongo.db.users.update(
            {"username": username}, {"$set": {"location": request.form.get("location")}})
        mongo.db.users.update(
            {"username": username}, {"$set": {"profile_picture": request.form.get("profile-picture")}})
        mongo.db.users.update(
            {"username": username}, {"$set": {"about": request.form.get("about")}})
        mongo.db.users.update(
            {"username": username}, {"$set": {"interest": request.form.get("interest")}})
        return redirect(url_for("profile"))
    return render_template("edit_profile.html", username=username,
                           location=location, email=email, about=about,
                           interest=interest, profile_picture=profile_picture)


@app.errorhandler(404)
def page_not_found(e):

    if session["user"] != "":
        return render_template('404.html'), 404
    else:
        return render_template('not-logged-in.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 500


def profile_picture_finder(username):
    picture = mongo.db.users.find_one(
        {"username": username})["profile_picture"]
    return picture


def logged_in_test():
    if session["user"] == "":
        return False
    else:
        return True


@ app.context_processor
def context_processor():
    return dict(profile_picture_finder=profile_picture_finder)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
