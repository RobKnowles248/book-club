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


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = mongo.db.books.find({"$text": {"$search": query}})
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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


def compute_average_score(book):
    scores = []
    for review in book["reviews"]:
        scores.append(review["score"])
    print(scores)
    return sum(scores) // len(scores)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        # Find the book in the db
        book = mongo.db.books.find_one(
            {"book_name": request.form.get("choose_book")}
        )

        if book:
            # Check if the user has already reviewed this book
            for review in book["reviews"]:
                if review["review_author"] == session["user"]:
                    flash("You have already reviewed this book!")
                    return redirect(url_for("add_review"))

            else:
                # Store the new review data as a dictionary
                new_review = {
                    "score": int(request.form.get("stars")),
                    "review_text": request.form.get("review_text"),
                    "review_author": session["user"]
                }
                print(new_review)

                # Add the new review data to the dictionary we will update
                book["reviews"].append(new_review)

                # Compute the new average score
                book["average_score"] = compute_average_score(book)
                print(book)

                # Add the review data to the book's data in the db
                mongo.db.books.update({"book_name": book["book_name"]}, book)
                flash("Review Successfully Added!")
                return redirect(url_for("index"))

        else:
            flash("Book not found!")
            return redirect(url_for("add_review"))

    books = mongo.db.books.find().sort("book_name", 1)
    return render_template("add_review.html", books=books)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        # Check if the book already exists
        existing_book = mongo.db.books.find_one(
            {"book_name": request.form.get("book_name")}
        )
        if existing_book:
            flash("Book already exists!")
            return redirect(url_for("add_review"))
        else:
            # Store the new book data in a dictionary
            new_book = {
                "book_name": request.form.get("book_name"),
                "author": request.form.get("author"),
                "img_url": "",
                "purchase_link": "",
                "average_score": 1,
                "reviews": []
            }

            # Add the new book to the db
            mongo.db.books.insert_one(new_book)
            flash("Book Successfully Added!")
            return redirect(url_for("add_review"))

    return render_template("add_book.html")


@app.route("/book_page/<book_id>")
def book_page(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("book_page.html", book=book)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
