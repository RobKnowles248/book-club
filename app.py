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
@app.route("/index")
def index():
    books = mongo.db.books.find()
    return render_template("index.html", books=books)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    # code for this method adapted from code for the
    # register method in the task manager mini project.
    if request.method == "POST":
        # first check if the username already exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("signup"))

        # check if passwords match
        confirm = request.form.get("confirm-password")
        password = request.form.get("password")
        if confirm != password:
            flash("Passwords do not match")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }

        mongo.db.users.insert_one(signup)

        # put the new user into the 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Signup Successful!")
        return redirect(url_for("index"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # code for this method adapted from code for the
    # login method in the task manager mini project.
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if hashed password matches the one in db
            password_check = check_password_hash(
                existing_user["password"], request.form.get("password"))

            if password_check:
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for("index"))

            else:
                # password did not match
                flash("Incorrect Username and/or Password!")
                return redirect(url_for("login"))

        else:
            # username not found
            flash("Incorrect Username and/or Password!")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("Successfully logged out!")
    session.pop("user")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
