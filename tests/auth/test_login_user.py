import allure
import requests
from data import Urls, ApiResponse


class TestLoginUser:

    @allure.title('Успешная авторизация ')
    @allure.description("Проверка успешной авторизации,проверка кода и текста ответа ")
    def test_authorization_user_successfully(self,register_new_user_and_return_login_password):
        payload = {
            "email": register_new_user_and_return_login_password[0],
            "password": register_new_user_and_return_login_password[1]
            }
        response = requests.post(Urls.LOGIN_USER, data=payload)
        assert response.status_code == 200 and ApiResponse.RESPONSE_SUCCESSFULLY_LOGIN in response.text




    @allure.title('Авторизация с указанием некоррекных данных')
    @allure.description("Проверка  ошибки авторизации пользователя с некоррекными данными")
    def test_user_authorization_with_incorrect_data(self, create_data_for_user):
        payload = {
            "email": create_data_for_user[0],
            "password": create_data_for_user[1]
        }
        response = requests.post(Urls.LOGIN_USER, data=payload)
        assert response.status_code == 401 and response.text == ApiResponse.ERROR_401_INCORRECT

