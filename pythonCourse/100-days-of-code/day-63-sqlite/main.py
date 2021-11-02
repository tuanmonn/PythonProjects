from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create db using SQLite
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


# create db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, unique=True, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title

db.create_all()

# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()


## -- old ways to keep a dictionary of books --
# all_books = []
# dict = {}
# dict["book"] = request.form["book_name"]
# dict["author"] = request.form["author"]
# dict["rating"] = request.form["rating"]
# all_books.append(dict)
# print(all_books)


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        # add books to database
        new_book = Book(title=request.form["book_name"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()

    all_books = db.session.query(Book).all()

    if len(all_books) == 0:
        msg = "There's no book in your lib"
        return render_template("index.html", msg=msg)
    else:
        return render_template("index.html", all_books=all_books)

@app.route('/update_rating', methods=["GET","POST"])
def update_rating():
    if request.method == "POST":
        # update the book rating
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for('home'))
    all_books = db.session.query(Book).all()
    return render_template("index.html", all_books=all_books)


@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/edit?id=<id>")
def edit(id):
    book_to_display = Book.query.filter_by(id=id).first()
    return render_template("edit.html", book_name= book_to_display.title, book_rating= book_to_display.rating, book_id= book_to_display.id)

if __name__ == "__main__":
    app.run(debug=True)
