
# this is the "web_app/routes/stocks_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash


from app.weather import to_image, chopped_date, display_forecast

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather")
def weather_form():
    print("7 days weather forecast...")
    return render_template("weather_form.html")
