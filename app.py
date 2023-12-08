from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/home")
def home():
    pass


@app.route("/aboutme")
def aboutMe():
    pass


@app.route("/contactMe")
def contactMe():
    pass


@app.route("projects")
def projects():
    pass

@app.route("menaBlogs")
def myBlogs():
    pass


if __name__ == "__main__":
    app.run(debug=True)
