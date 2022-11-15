from abc import abstractmethod

baseurl = "https://petstore.swagger.io/v2"


POST_create_user = baseurl + "/user"

GET_find_purchase_order_by_ID = baseurl + "/store/order/{}"

GET_get_user_by_user_name = baseurl + "/user/{}"

DELETE_delete_user = baseurl + "/user/{}"
