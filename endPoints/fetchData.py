import requests
import json
import jsonpath

from env.urls import *


def creteUser(name):
    data = {
        "id": 0,
        "username": name,
        "firstName": "mirza",
        "lastName": "jijieshvili",
        "email": "mirzajijieshvili@gmail.com",
        "password": "123",
        "phone": "123123123",
        "userStatus": 1
    }
    headers = {'Content-Type': "application/json", 'Accept': "application/json"}
    r = requests.post(POST_create_user, data=json.dumps(data), headers=headers)
    print(r.status_code)


def getFindPurchaseOrderByID(ID):
    response = requests.get(GET_find_purchase_order_by_ID.format(ID))

    json_response = json.loads(response.text)

    responseBody = response.content

    responseHeader = response.headers

    print(response)
    print(json_response)

    quantity = jsonpath.jsonpath(json_response, "quantity")

    print(quantity[0])
    assert quantity[0] == 2
    # assert quantity[0] == 5
    print(responseBody)

    print(responseHeader)


def getUserByUserName(userName):
    response = requests.get(GET_get_user_by_user_name.format(userName))

    json_response = json.loads(response.text)

    responseBody = response.content

    responseHeader = response.headers

    print(response)

    print(json_response)

    print(responseBody)

    print(responseHeader)

    user = jsonpath.jsonpath(json_response, "username")

    print(user[0])

    return user[0]
