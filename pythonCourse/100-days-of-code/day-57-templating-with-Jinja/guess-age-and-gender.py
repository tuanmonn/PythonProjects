from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


@app.route('/guess/<user_name>')
def guess(user_name):
    params = {"name": user_name}
    api_gender = requests.get(url="https://api.genderize.io", params=params)
    data_genderize = api_gender.json()
    api_age = requests.get(url="https://api.agify.io", params=params)
    data_age = api_age.json()
    name = data_genderize["name"]
    name_cap = name.title()
    gender = data_genderize["gender"]
    age = data_age["age"]
    return render_template("genderize.html", name= name_cap, gender= gender, age= age)

if __name__ == "__main__":
    app.run(debug=True)