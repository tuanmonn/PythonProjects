from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
from flask import jsonify

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dict ={}
        # go through all the columns in the table
        for column in self.__table__.columns:
            # get the column name - get the value of that column
            dict[column.name] = getattr(self, column.name)
        return dict


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # This is automatic
    return jsonify(cafe=random_cafe.to_dict())

    # This is manual
    # return jsonify(id=random_cafe.id,
    #                name=random_cafe.name,
    #                map_url=random_cafe.map_url,
    #                img_url=random_cafe.img_url,
    #                location=random_cafe.location,
    #                seats=random_cafe.seats,
    #                has_toilet=random_cafe.has_toilet,
    #                has_wifi=random_cafe.has_wifi,
    #                has_sockets=random_cafe.has_sockets,
    #                can_take_calls=random_cafe.can_take_calls,
    #                coffee_price=random_cafe.coffee_price)
    
@app.route("/all")
def get_all_cafe():
    cafes = db.session.query(Cafe).all()
    cafe_dict = {}
    for cafe in cafes:
        cafe_dict[cafe.name] = cafe.to_dict()
    return jsonify(cafe=cafe_dict)

@app.route("/search")
def search_cafe():
    # specify a query parameter called "loc", take the value of that query param
    query_location = request.args.get("loc")
    specific_cafe = Cafe.query.filter_by(location=query_location).first()
    if specific_cafe:
        return jsonify(your_cafe=specific_cafe.to_dict())
    else:
        return jsonify(error={"Error": "Not found"})




## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
