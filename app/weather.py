degree_sign = u"\N{DEGREE SIGN}"

#import pgeocode
from pgeocode import Nominatim
import json
import requests

nomi = Nominatim('US')
geo = nomi.query_postal_code("07302")


latitude = geo["latitude"]
longitude = geo["longitude"]

request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
# print(request_url)
response = requests.get(request_url)
parsed_response = json.loads(response.text)

print(response.status_code)
parsed_response