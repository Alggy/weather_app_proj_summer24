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
    demo_test = display_forecast("10001")
    assert isinstance(demo_test,HTML)
