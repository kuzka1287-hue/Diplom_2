import allure
import requests
from data import BASE_URL, ORDERS_ENDPOINT, INGREDIENT_IDS, INVALID_INGREDIENT_HASH

@allure.feature("Заказы")
class TestOrderCreation:

    @allure.title("Создание заказа с неверным хешем ингредиента")
    def test_create_order_invalid_ingredient_hash(self, auth_token):
        url = BASE_URL + ORDERS_ENDPOINT
        payload = {"ingredients": [INVALID_INGREDIENT_HASH]}
        headers = {"Authorization": auth_token}
        response = requests.post(url, json=payload, headers=headers)
        assert response.status_code == 500
