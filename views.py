from flask import Blueprint, render_template, url_for

views = Blueprint(__name__, 'views')

@views.route("/")
def home():
    return render_template("homepage.html")

@views.route("/input")
def input():
    return render_template("input.html")