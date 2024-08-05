class Config:
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    LOGIN_URL = f"{BASE_URL}login"
    REGISTER_URL = f"{BASE_URL}register"
    FORGOT_PASSWORD_URL = f"{BASE_URL}forgot-password"

    TEST_USER_EMAIL = "lisasolominskaia12666@yandex.ru"
    TEST_USER_PASSWORD = "123456"
    ERROR_PASSWORD = "12345"

    ERROR_MESSAGE = "Некорректный пароль"
    LOGIN_BUTTON_TEXT = "Войти"
    MAIN_LOGIN_BUTTON_TEXT = "Войти в аккаунт"
    PERSONAL_ACCOUNT_TEXT = "Личный Кабинет"
    CONSTRUCTOR_BUTTON_TEXT = "Конструктор"
    LOGOUT_BUTTON_TEXT = "Выход"
