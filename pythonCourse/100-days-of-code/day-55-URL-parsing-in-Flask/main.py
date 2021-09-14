from flask import Flask

app = Flask(__name__)

@app.route("/") # run the following function when at the homepage
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p> this is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif?cid=ecf05e47rbdwbzq5vwbmv5q7emmtv51t230u7w6g3srjaxw6&rid=giphy.gif&ct=g" width=200px> '


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name}, you are {number} years old!"


def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)