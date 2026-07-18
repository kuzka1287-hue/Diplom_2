import pytest
from helpers import register_user, delete_user
from utils import generate_user_data

@pytest.fixture
def registered_user():
    """Создаёт пользователя и возвращает его данные и токен. После теста удаляет."""
    user_data = generate_user_data()
    response = register_user(user_data)
    json_data = response.json()
    access_token = json_data.get("accessToken")
    yield {"user": user_data, "access_token": access_token}
    if access_token:
        delete_user(access_token)

@pytest.fixture
def auth_token(registered_user):
    """Возвращает accessToken зарегистрированного пользователя."""
    return registered_user["access_token"]
