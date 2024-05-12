
import allure
import requests
from data import Urls, ApiResponse



class TestCreateOrder:

    @allure.title('Создание заказа с ингредиентами при авторизованном пользователе ')
    @allure.description("Проверка успешного создания заказа,проверка кода и текста ответа ")
    def test_create_order_with_authorization_and_ingedients(self,register_new_user_and_return_login_password):
        payload = {
            "email": register_new_user_and_return_login_password[0],
            "password": register_new_user_and_return_login_password[1]
        }
        response = requests.post(Urls.LOGIN_USER, data=payload)
        list_ingedients = requests.get(Urls.GET_INGREDIENTS)
        payload_ingedients = {"ingredients": [list_ingedients.json()["data"][0]["_id"]]}
        response_order = requests.post(Urls.ACTIONS_WITH_ORDERS, data=payload_ingedients,
                                 headers={'authorization': response.json()["accessToken"]})
        assert response_order.status_code == 200 and ApiResponse.RESPONSE_SUCCESSFULLY in response_order.text




    @allure.title('Создание заказа с ингредиентами  без авторизозации пользователя ')
    @allure.description("Тестирование создания заказа,проверка кода и текста ответа ")
    def test_create_order_withowt_authorization(self):
        list_ingedients = requests.get(Urls.GET_INGREDIENTS)
        payload_ingedients = {"ingredients": [list_ingedients.json()["data"][0]["_id"]]}
        response_order = requests.post(Urls.ACTIONS_WITH_ORDERS, data=payload_ingedients)
        assert response_order.status_code == 200 and ApiResponse.RESPONSE_SUCCESSFULLY in response_order.text
        # В документации нет информации какой должен быть ответ, если нет авторизации.
        # Ответ найден методом запросов через postman.




    # В виду того, что заказ успешно создается и без авторизации, посчитал что делать по 2 одинаковых теста
    # на каждое условие будет лишним.

    @allure.title('Создание заказа без ингредиентов')
    @allure.description("Тестирование создания заказа без ингредиентов ,проверка кода и текста ответа ")
    def test_create_order_withowt_ingedients(self):
        payload_ingedients = {"ingredients": []}
        response_order = requests.post(Urls.ACTIONS_WITH_ORDERS, data=payload_ingedients)
        assert response_order.status_code == 400 and ApiResponse.ERROR_400_BAD_REQUEST in response_order.text

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    @allure.description("Тестирование создания заказа с неверным хешем ингредиентов ,проверка кода и текста ответа ")
    def test_create_order_with_incorrect_ingredient_hash(self):
        payload_ingedients = {"ingredients": ["iuhsaegasg"]}
        response_order = requests.post(Urls.ACTIONS_WITH_ORDERS, data=payload_ingedients)
        assert response_order.status_code == 500 and ApiResponse.ERROR_500_INTERNAL_SERVER_ERROR in response_order.text