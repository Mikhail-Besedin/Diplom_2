

import allure
import pytest
import requests

import helpers
from data import ApiResponse, Urls


class TestChangeUsersData:
    @pytest.mark.parametrize('value', ["email", "password", "name"])
    @allure.title('Изменение данных пользователя с авторизацией')
    @allure.description("Проверка успешного изменение данных пользователя с авторизацией,проверка кода и текста ответа ")
    def test_changing_user_data_with_authorization_successfully(self,register_new_user_and_return_login_password, value):
        payload = {
            "email": register_new_user_and_return_login_password[0],
            "password": register_new_user_and_return_login_password[1],
            "name": register_new_user_and_return_login_password[2]
        }
        response_login = requests.post(Urls.LOGIN_USER, data=payload)
        payload_changing = {value:helpers.generate_random_string(10)}
        response_changing = requests.patch(Urls.ACTIONS_WITH_USER, data=payload_changing,
                                           headers={'authorization': response_login.json()["accessToken"]})
        assert response_changing.status_code == 200 and ApiResponse.RESPONSE_SUCCESSFULLY in response_changing.text



    @pytest.mark.parametrize('value', ["email", "password", "name"])
    @allure.title('Изменение данных пользователя без авторизации')
    @allure.description("Проверка изменение данных пользователя без авторизации,проверка кода и текста ошибки ")
    def test_changing_user_data_withowt_authorization_error(self,register_new_user_and_return_login_password, value):
        payload_changing = {value:helpers.generate_random_string(10)}
        response = requests.patch(Urls.ACTIONS_WITH_USER, data=payload_changing)
        assert response.status_code == 401 and ApiResponse.ERROR_401_UNAUTHORIZED in response.text
