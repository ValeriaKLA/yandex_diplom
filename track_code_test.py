import configuration
import send_request
import data
import requests

#проверить что по треку заказа можно получить данные о заказе

def get_order():
    return send_request.post_new_order(data.order_body)

def get_track_number(response):
    response_json = response.json()
    track_number = response_json.get("track")
    return {"t": track_number}

def get_order_by_track(track):
    track_str = "?t=" + str(track["t"])
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + track_str)

def positive_assert(response, expected_status = 201):
    assert response.status_code == expected_status, f"Expected status {expected_status}, got {response.status_code}"

# Валерия Козицина, 17-я когорта - Финальный проект. Инженер по тестированию плюс
def test_create_and_get_order():
    response_order = get_order()
    positive_assert(response_order)

    order_track = get_track_number(response_order)

    response_get_order = get_order_by_track(order_track)
    positive_assert(response_get_order, expected_status = 200)
