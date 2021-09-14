from flask import Flask

app = Flask(__name__)

@app.route("/") # run the following function when at the homepage
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()