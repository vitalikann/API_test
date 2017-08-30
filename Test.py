import requests
import json
from jsonschema import validate

# data for request
url = "http://qapediaq.webprv.com/api/auth/login"

header = {
        "Version": "28"
        }

data = {
        "email": "2kec@gmail.com",
        "password": "12345678"
        }
# getting response
response = requests.post(url, data=data, headers=header)

# extract data from response and saving token for the next test
token = response.json()["token"]

# open and load json scheme file
schema_file = open("login.json", "r")
schema_json = json.load(schema_file)

# validation
validate(response.json(), schema_json)

# close json scheme file
schema_file.close()



