# this is the "test/stocks_test.py" file...

def test_example():
    assert 2 + 2 == 4

#from pandas import DataFrame
from app.weather import degree_sign, display_forecast

def test_degree_formatting():
    assert f"90 {degree_sign}F" == "90 °F"


def test_data_fetching():
    df = display_forecast("10001")
    assert isinstance(df,DataFrame)