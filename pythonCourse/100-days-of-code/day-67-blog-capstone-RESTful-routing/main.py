from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##INIT THE CKEDITOR
ckeditor = CKEditor()

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all() # have this so it will query every time the page is redirected
    return render_template("index.html", all_posts=posts)


# -- Below code will not update the data after it's edited
# because the posts data is still old. We need to query it again
# so that it will not be cached --

# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#     requested_post = None
#     for blog_post in posts:
#         if blog_post.id == post_id:
#             requested_post = blog_post
#     return render_template("post.html", post=requested_post)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)

@app.route("/new-post", methods=["GET","POST"])
def new_post():
    form = CreatePostForm()
    header = "New Post"
    if form.validate_on_submit():
        time = datetime.datetime.now()
        post = BlogPost(title=form.title.data,
                        subtitle=form.subtitle.data,
                        author=form.author.data,
                        img_url=form.img_url.data,
                        body=form.body.data,
                        date=f"{time.strftime('%B')} {time.day}, {time.year}"
                        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form, header=header)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/edit-post/<post_id>", methods=["GET","POST"])
def edit_post(post_id):
    header = "Edit Post"
    post = BlogPost.query.filter_by(id=post_id).first()
    edit_form = CreatePostForm(title=post.title,
                          subtitle=post.subtitle,
                          author=post.author,
                          img_url=post.img_url,
                          body=post.body)
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))
    return render_template("make-post.html", header=header, form=edit_form)

@app.route("/delete/<int:post_id>")
def delete(post_id):
    BlogPost.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)