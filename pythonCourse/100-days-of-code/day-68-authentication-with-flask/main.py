import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_gravatar import Gravatar
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user



app.config['SECRET_KEY'] = '47751B3685592'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    UserMixin()
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

#Line below only required once, when creating DB.
# db.create_all()

# Create login manager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods= ["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()
        if user:
            error = "This email has already been registered. Log in instead."
            return render_template('login.html', error=error)
        else:
            hash_pwd = werkzeug.security.generate_password_hash(request.form["password"], method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=request.form["email"], password=hash_pwd, name=request.form["name"])
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('secrets'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if not user:
            error = "Your email is wrong, son."
        elif check_password_hash(user.password, password):
            login_user(user)
            flash("You were successfully logged in")
            return redirect(url_for('secrets'))
        else:
            error = "Wrong password, son."
    return render_template('login.html', error=error, logged_in=current_user.is_authenticated)



@app.route('/secrets')
@login_required
def secrets():
    logged_in = True
    return render_template("secrets.html", user_name = current_user.name, logged_in = logged_in)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files',
                               "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
