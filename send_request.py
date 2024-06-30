import configuration
import requests
import data

def post_new_order(body): #клиент создает заказ
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json = body)
response = post_new_order(data.order_body)
