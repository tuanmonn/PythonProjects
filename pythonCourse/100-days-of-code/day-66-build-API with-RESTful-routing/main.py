from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
from flask import jsonify

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

secret_api_key = "123456"

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(250), nullable=True)
    seats = db.Column(db.String(250), nullable=True)
    has_toilet = db.Column(db.Boolean, nullable=True)
    has_wifi = db.Column(db.Boolean, nullable=True)
    has_sockets = db.Column(db.Boolean, nullable=True)
    can_take_calls = db.Column(db.Boolean, nullable=True)
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


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_price(id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.filter_by(id=id).first()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": "Successfully updated the price"}),200
    else:
        return jsonify({"Error": "We couldn't find the cafe with that id"}),404

@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    api_key = request.args.get("api_key")
    cafe = Cafe.query.filter_by(id=id).first()
    if api_key == secret_api_key:
        if cafe:
            Cafe.query.filter_by(id=id).delete()
            db.session.commit()
            return jsonify({"Success": "We have deleted that cafe!"})
        else:
            return jsonify({"Error": "We couldn't find the cafe with that id"}), 404
    else:
        return jsonify({"Error": "You don't have the permission to delete cafe"})


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
