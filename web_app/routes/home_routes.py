# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash
from app.weather import to_image, chopped_date, display_forecast

home_routes = Blueprint("home_routes", __name__)



@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("zip.html")