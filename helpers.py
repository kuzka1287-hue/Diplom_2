import requests
from data import BASE_URL, REGISTER_ENDPOINT, LOGIN_ENDPOINT
from utils import generate_user_data  # если есть

def register_user(user_data):
    url = BASE_URL + REGISTER_ENDPOINT
    return requests.post(url, json=user_data)

def login_user(login_data):
    url = BASE_URL + LOGIN_ENDPOINT
    return requests.post(url, json=login_data)

def delete_user(access_token):
    # Если есть эндпоинт удаления, иначе можно использовать refreshToken для выхода
    # Например, если есть DELETE /api/auth/user
    # url = BASE_URL + "/api/auth/user"
    # headers = {"Authorization": access_token}
    # return requests.delete(url, headers=headers)
    # Если эндпоинта нет, можно просто ничего не делать
    pass
