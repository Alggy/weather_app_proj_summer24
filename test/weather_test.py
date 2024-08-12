# this is the "test/stocks_test.py" file...

from app.weather import degree_sign, display_forecast
from IPython.core.display import HTML
from pgeocode import Nominatim
import requests
import json
from IPython.display import Image, display
from IPython.core.display import HTML
from pandas import DataFrame

def test_degree_formatting():
    assert f"90 {degree_sign}F" == "90 °F"


def test_demo():
    df = display_forecast("10001")
    assert isinstance(df,DataFrame)
    assert df.columns.tolist() == ['day', 'date', 'temp', 'forecast', 'icon']

def test_location():
    nomi = Nominatim("US")
    nomi.query_postal_code("10001")["place_name"] == "New York"
    nomi.query_postal_code("07302")["place_name"] == "Jersey City"
    nomi.query_postal_code("15201")["place_name"] == "Pittsburgh"