from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = date.today().year
    user_name = "Tuanmonn"
    return render_template("index.html", num=random_number, year = current_year, name = user_name)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts= all_posts)


if __name__ == "__main__":
    app.run(debug=True)