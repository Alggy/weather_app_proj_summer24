# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash
from app.weather import to_image, chopped_date, display_forecast

home_routes = Blueprint("home_routes", __name__)



@home_routes.route("/")
@home_routes.route("/home")
def zip_input():
    print("Enter a ZIP Code...")
    #return "Welcome Home"
    return render_template("zip.html")

@home_routes.route("/weather", methods=["GET", "POST"])
def weather_forecast():
    print("7 Days Forecast...")
    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)

    print("REQUEST DATA:", request_data)

    zip = request_data.get("zip") or "10001" # get specified symbol or use default

    try:
        weather = display_forecast(zip=zip)

        #flash("Fetched Real-time Market Data!", "success")
        return render_template("forecast.html",
            zip=zip
        )
    except Exception as err:
        print('OOPS', err)

        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/")



    