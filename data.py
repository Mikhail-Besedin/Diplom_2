class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    GET_INGREDIENTS = BASE_URL + "/api/ingredients"
    ACTIONS_WITH_ORDERS = BASE_URL + "/api/orders"
    LOGIN_USER = BASE_URL + "/api/auth/login"
    ACTIONS_WITH_USER = BASE_URL + "/api/auth/user"
    CREATE_USER = BASE_URL + "/api/auth/register"



class ApiResponse:
    ERROR_400_BAD_REQUEST = '{"success":false,"message":"Ingredient ids must be provided"}'
    ERROR_401_INCORRECT = '{"success":false,"message":"email or password are incorrect"}'
    ERROR_401_UNAUTHORIZED = '{"success":false,"message":"You should be authorised"}'
    ERROR_403_EXISTING = '{"success":false,"message":"User already exists"}'
    ERROR_403_FORBIDDEN = '{"success":false,"message":"Email, password and name are required fields"}'
    ERROR_500_INTERNAL_SERVER_ERROR = "Internal Server Error"

    RESPONSE_SUCCESSFULLY = '"success":true'
    RESPONSE_SUCCESSFULLY_LOGIN = '"refreshToken"'
