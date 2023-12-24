import request


#Токарева Дарья, 11-ая когорта "Финальный проект, инженер по тестированию"
# Тест проверки создания заказа
def test_order_creation():
        creation_response = request.post_new_order()
        response = request.get_orders_track()
        assert response.status_code == 200
