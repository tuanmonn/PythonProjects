# task: make a python decorator function to bold, underline and italicize the text using HTML

from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return f"Hello there!"

def make_bold(function):
    def wrap_func():
        result = function()
        return f"<b>{result}</b>"
    return wrap_func

def make_underline(function):
    def wrap_func():
        result = function()
        return f"<u>{result}</u>"
    return wrap_func

def make_italic(function):
    def wrap_func():
        result = function()
        return f"<em>{result}</em>"
    return wrap_func

@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)