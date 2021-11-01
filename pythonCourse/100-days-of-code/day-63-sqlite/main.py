from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, unique=True, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title

db.create_all()
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()

all_books = []


@app.route('/')
def home():
    if len(all_books) == 0:
        msg = "There's no book in your lib"
        return render_template("index.html", msg=msg)
    else:
        return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        dict = {}
        dict["book"] = request.form["book_name"]
        dict["author"] = request.form["author"]
        dict["rating"] = request.form["rating"]
        all_books.append(dict)
        print(all_books)

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
