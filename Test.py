import random
import requests
import json

from jsonschema import validate

server = "http://qapediaq.webprv.com"


def validate_json_chema(file, r):
    # open and load json scheme file
    schema_file = open(file, "r")
    schema_json = json.load(schema_file)

    # validation
    validate(r.json(), schema_json)

    # close json scheme file
    schema_file.close()

    print(r.content)


def test_login():
    # data for request
    url = server + "/api/auth/login"

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

    validate_json_chema("login.json", response)

    return token


def test_addchild():
    # data for request
    url = server + "/api/parent/addchild"

    header = {
        "Version": "28"
    }

    data = {
        "token": token,
        "birthday": "2010-10-16",
        "first_name": "test first name" + str(random.randrange(1000)), # we cannot create another child with the same name
        "gender": "female",
        "last_name": "test last name"
    }

    # getting response
    response = requests.post(url, data=data, headers=header)

    validate_json_chema("addchild.json", response)


test_login()
test_addchild()