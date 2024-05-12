import allure
import pytest
import requests


from data import ApiResponse, Urls
from helpers import generate_random_string


class TestCreateUser:
    @allure.title('Успешное создание пользователя')
    @allure.description("Создание пользователя, проверка кода и текста ответа")
    def test_create_user_successfully(self, create_data_for_user):
        payload = {
            "email": create_data_for_user[0],
            "password": create_data_for_user[1],
            "name": create_data_for_user[2]}
        response = requests.post(Urls.CREATE_USER, data=payload)
        assert response.status_code == 200 and ApiResponse.RESPONSE_SUCCESSFULLY in response.text




    @allure.title("Невозможно создать пользователя, который уже зарегистрирован")
    @allure.description("Проверка статус кода и текста ошибки при создании пользователей с одинаковыми логинами и паролями")
    def test_create_user_with_the_same_data(self,register_new_user_and_return_login_password):
        payload = {
            "email": register_new_user_and_return_login_password[0],
            "password": register_new_user_and_return_login_password[1],
            "name": register_new_user_and_return_login_password[2]}
        response = requests.post(Urls.CREATE_USER, data=payload)
        assert response.status_code == 403 and response.text == ApiResponse.ERROR_403_EXISTING





    email = generate_random_string(7) + f'@yandex.ru'
    password = generate_random_string(7)
    name = generate_random_string(7)
    @pytest.mark.parametrize("email,password,name",[
                             (email,password,""),
                             (email,"", name),
                             ("",password, name)])
    @allure.title("Попытка создать пользователя без указания одного из обязательных полей")
    @allure.description("Проверка статус кода и текста ошибки  при попытки создания пользователя,"
                        " не заполнив одно из обязательных полей")
    def test_create_user_withowt_one_fields(self, email,password,name):
        payload = {
            "email": email,
            "password": password,
            "name": name}
        response = requests.post(Urls.CREATE_USER, data=payload)
        assert response.status_code == 403 and response.text == ApiResponse.ERROR_403_FORBIDDEN


