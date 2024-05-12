import allure
import pytest
import requests
from data import Urls
from helpers import generate_random_string



@allure.step("Генерируем данные для создания пользователя и возвращаем список из логина, пароля и имени.")
@pytest.fixture()
def create_data_for_user():
    email = generate_random_string(7)+ f'@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(7)

    login_pass = []
    login_pass.append(email)
    login_pass.append(password)
    login_pass.append(name)

    return login_pass



@allure.step("регистрируем нового пользователя и возвращаем список из с данными для регистрации,"
             " После прохождения теста удаляем пользователя.")
@pytest.fixture()
def register_new_user_and_return_login_password(create_data_for_user):

    login_pass = create_data_for_user
    payload = {
        "email": create_data_for_user[0],
        "password": create_data_for_user[1],
        "name": create_data_for_user[2]}
    response = requests.post(Urls.CREATE_USER, data=payload)

    yield login_pass

    response_delete = requests.delete(Urls.ACTIONS_WITH_USER, headers={'authorization': response.json()["accessToken"]})
    return response_delete