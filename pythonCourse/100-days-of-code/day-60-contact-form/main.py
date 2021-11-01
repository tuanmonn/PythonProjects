from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
url = 'https://api.npoint.io/ed99320662742443cc5b'
get_blog = requests.get(url)
blog_posts = get_blog.json()
author = "Tuanmonn"
my_email = "test@gmail.com"
my_password = "testPassword()"

@app.route('/')
def home():
    return render_template("index.html", blog_posts= blog_posts, author= author)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<int:id>')
def post_page(id):
    return render_template("post.html", blog_posts= blog_posts, author= author, id=id)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_name = request.form["username"]
        user_email = request.form["useremail"]
        user_phone = request.form["userphone"]
        user_message = request.form["usermessage"]
        contact_success = "Your message has reached my inbox!"
        contact_success_extra = "I'll get back to you as soon as I can :D"

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="nguyenhung.tuan@aiesec.net",
                                msg=f"Subject:New blog message!\n\n A person called '{user_name}' with the email {user_email} and phone number {user_phone} sent you this message:\n{user_message}")

        return render_template("contact.html", msg = contact_success, msg_extra = contact_success_extra)
    else:
        main_fallback = "Contact me"
        sub_fallback = "What do you want to tell me?"
        return render_template("contact.html", main_fallback= main_fallback, sub_fallback= sub_fallback)

if __name__ == "__main__":
    app.run(debug=True)