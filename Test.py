import requests
import json

from jsonschema import validate

def validate_json_chema():
    return

def test_login():
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
    global token
    token = response.json()["token"]

# open and load json scheme file
    schema_file = open("login.json", "r")
    schema_json = json.load(schema_file)

# validation
    validate(response.json(), schema_json)

# close json scheme file
    schema_file.close()

    return token

def test_addchild():
# data for request
    url = "http://qapediaq.webprv.com/api/parent/addchild"

    header = {
        "Version": "28"
    }

    data = {
        "token": token,
        "birthday": "2010-10-16",
        "first_name": "test first name",
        "gender": "female",
        "last_name": "test last name"
    }

# getting response
    response = requests.post(url, data=data, headers=header)

# open and load json scheme file
    schema_file = open("addchild.json", "r")
    schema_json = json.load(schema_file)

# validation
    validate(response.json(), schema_json)

# close json scheme file
    schema_file.close()

test_login()
test_addchild()
