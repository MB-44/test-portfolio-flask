from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home/home.html",title = "menath.dev")

@app.route("/aboutme")
def aboutMe():
    return render_template("about_me/about_me.html",title = "About Me")


@app.route("/contactMe")
def contactMe():
    return render_template("contact_me/contact_me.html",title = "Contact me")


@app.route("/projects")
def projects():
    return render_template("projects/projects.html",title = "Projects")

@app.route("/menaBlogs")
def myBlogs():
    return render_template("blogs/my_blogs.html",title = "Menaa Blogs")


if __name__ == "__main__":
    app.run(debug=True)
