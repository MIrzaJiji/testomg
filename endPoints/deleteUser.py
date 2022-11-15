import json
import jsonpath
from env.urls import *
import requests


pathParam = "jiji"

queryParam = {

}

def deleteUserByName(name):

    response = requests.delete(DELETE_delete_user.format(name))

    print(DELETE_delete_user.format(pathParam))
    print(response)
    print(response.status_code)
