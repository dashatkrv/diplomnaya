import configuration
import requests
import data



def post_new_order(): # запрос на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,  # подставялем полный url
                         json=data.order_body)  # а здесь тело



def get_orders_track(): # запрос на получение заказа по его трек номеру
     return requests.get(configuration.URL_SERVICE + "?t=" + str(configuration.RECEIVING_ORDER_BY_ID))
     response.track_id = creation_response.json()['track']