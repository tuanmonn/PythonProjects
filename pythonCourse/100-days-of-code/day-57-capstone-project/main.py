from flask import Flask, render_template
import requests

app = Flask(__name__)

url = 'https://api.npoint.io/ed99320662742443cc5b'
get_blog = requests.get(url)
blog_data = get_blog.json()

@app.route('/')
def home():
    return render_template("index.html", posts= blog_data)

@app.route('/post/<int:blog_id>')
def post_page(blog_id):
    return render_template("post.html", posts= blog_data, post_id= blog_id)

if __name__ == "__main__":
    app.run(debug=True)
