from functools import wraps
from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from sqlalchemy import Integer, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = '4sgXgurXxkMySCRKtZcHA7HzZldWvES7'
ckeditor = CKEditor(app)
Bootstrap(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)

##CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "User"
    UserMixin()
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250), nullable=False)
    user_password = db.Column(db.String(250))
    user_email = db.Column(db.String(250), nullable=False)
    posts = relationship('BlogPost', back_populates="author")
    comments = relationship('Comment', back_populates="comment_author")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(500))
    author_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    comments = relationship('Comment', back_populates="parent_post")
    author = relationship('User', back_populates="posts")

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    comment_author = relationship('User', back_populates="comments")
    parent_post = relationship('BlogPost', back_populates="comments")

db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts,
                           logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    form_register = RegisterForm()
    if form_register.validate_on_submit():
        if User.query.filter_by(user_email=form_register.email.data).first():
            flash("This email is already registered. Log in instead!")
            return redirect(url_for('login'))
        else:
            new_user = User(user_name=form_register.name.data,
                            user_email=form_register.email.data,
                            user_password=form_register.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form_register)


@app.route('/login', methods=["GET", "POST"])
def login():
    form_login = LoginForm()
    if form_login.validate_on_submit():
        if User.query.filter_by(user_email=form_login.email.data).first() and User.query.filter_by(user_password=form_login.password.data).first():
            login_user(User.query.filter_by(user_email=form_login.email.data).first())
            return redirect(url_for('get_all_posts'))
        elif not User.query.filter_by(user_email=form_login.email.data).first():
            flash("Wrong email son. Try again.")
        else:
            flash("Wrong password son. Try again.")
    return render_template("login.html", form=form_login, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    form_comment = CommentForm()
    if form_comment.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment")
            return redirect(url_for('login'))
        # add new comment
        new_comment = Comment(text=form_comment.comment.data, user_id=current_user.id, post_id=requested_post.id)
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=requested_post, form=form_comment, logged_in=current_user.is_authenticated)


@app.route("/about")
def about():
    return render_template("about.html", logged_in = current_user.is_authenticated)


@app.route("/contact")
def contact():
    return render_template("contact.html", logged_in = current_user.is_authenticated)


# Create decorator
def admin_only(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return wrapper_function


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            date=date.today().strftime("%B %d, %Y"),
            author_id= current_user.id
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, logged_in = current_user.is_authenticated)


@app.route("/edit-post/<int:post_id>")
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form, logged_in = current_user.is_authenticated)

@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'), logged_in = current_user.is_authenticated)

if __name__ == "__main__":
    app.run(debug=True)
