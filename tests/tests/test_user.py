import pytest
import allure
from data import BASE_URL, REGISTER_ENDPOINT, MSG_USER_EXISTS, MSG_REQUIRED_FIELDS
from helpers import register_user, delete_user
from utils import generate_user_data

@allure.feature("Пользователь")
class TestUserRegistration:

    @allure.title("Успешная регистрация уникального пользователя")
    def test_register_new_user_success(self):
        user_data = generate_user_data()
        response = register_user(user_data)
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["success"] is True
        assert "accessToken" in json_data
        # Удаляем после теста
        delete_user(json_data.get("accessToken"))

    @allure.title("Регистрация существующего пользователя")
    def test_register_existing_user_fails(self):
        user_data = generate_user_data()
        # Сначала регистрируем
        response1 = register_user(user_data)
        assert response1.status_code == 200
        # Пытаемся повторно
        response2 = register_user(user_data)
        assert response2.status_code == 403
        assert response2.json()["message"] == MSG_USER_EXISTS
        # Удаляем после теста
        delete_user(response1.json().get("accessToken"))

    @allure.title("Регистрация без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_register_missing_field_fails(self, missing_field):
        user_data = generate_user_data()
        del user_data[missing_field]
        response = register_user(user_data)
        assert response.status_code == 403
        assert response.json()["message"] == MSG_REQUIRED_FIELDS
        # Удалять нечего, т.к. пользователь не создан
