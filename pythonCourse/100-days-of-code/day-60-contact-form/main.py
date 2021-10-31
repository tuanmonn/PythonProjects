from flask import Flask, render_template, request
import requests

app = Flask(__name__)
url = 'https://api.npoint.io/ed99320662742443cc5b'
get_blog = requests.get(url)
blog_posts = get_blog.json()
author = "Tuanmonn"

@app.route('/')
def home():
    return render_template("index.html", blog_posts= blog_posts, author= author)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def post_page(id):
    return render_template("post.html", blog_posts= blog_posts, author= author, id=id)

@app.route('/thankyou', methods=["POST"])
def thankyou():
    user_name = request.form["username"]
    user_email = request.form["useremail"]
    user_phone = request.form["userphone"]
    user_message = request.form["usermessage"]
    return render_template("thankyou.html", name= user_name, email= user_email, phone=user_phone, message=user_message )


if __name__ == "__main__":
    app.run(debug=True)