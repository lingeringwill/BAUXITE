from flask import Blueprint
from flask import render_template

views = Blueprint('views',__name__)

@views.route("/")

def home():
    return "Hello there!"
    