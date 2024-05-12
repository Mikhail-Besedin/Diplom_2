import allure
import requests

from data import Urls, ApiResponse


class TestGetListOrder:
    @allure.title('Получение заказов конкретного пользователя c авторизацией')
    @allure.description("Проверка получения списка заказов пользователя c авторизацией, статус кода и в тексте ответа ")
    def test_get_orders_list_with_authorization(self,register_new_user_and_return_login_password):
        payload = {
            "email": register_new_user_and_return_login_password[0],
            "password": register_new_user_and_return_login_password[1]
        }
        response_login = requests.post(Urls.LOGIN_USER, data=payload)
        list_ingedients = requests.get(Urls.GET_INGREDIENTS)
        payload_ingedients = {"ingredients": [list_ingedients.json()["data"][0]["_id"]]}
        requests.post(Urls.ACTIONS_WITH_ORDERS, data=payload_ingedients,
                                       headers={'authorization': response_login.json()["accessToken"]})
        response = requests.get(Urls.ACTIONS_WITH_ORDERS,headers={'authorization': response_login.json()["accessToken"]})
        assert response.status_code == 200 and ApiResponse.RESPONSE_SUCCESSFULLY in response.text




    @allure.title('Получение заказов без авторизации ')
    @allure.description("Проверка получения списка заказов без авторизации, статус кода и в тексте ответа ")
    def test_get_orders_list_withowt_authorization(self):
        response = requests.get(Urls.ACTIONS_WITH_ORDERS)
        assert response.status_code == 401 and ApiResponse.ERROR_401_UNAUTHORIZED == response.text