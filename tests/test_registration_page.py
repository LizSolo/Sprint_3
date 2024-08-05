from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import Config
from locators import Locators

def test_successful_registration(driver, register_user, unique_user):
    name, email = unique_user
    register_user(name, email, Config.TEST_USER_PASSWORD)

    # Проверяем перенаправление на страницу входа
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Config.LOGIN_URL))
    assert driver.current_url == Config.LOGIN_URL


def test_registration_with_invalid_password(driver, register_user, unique_user):
    name, email = unique_user
    register_user(name, email, Config.ERROR_PASSWORD)

    # Ожидаем сообщение об ошибке
    error_message = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((Locators.ERROR_TEXT))
    )

    assert error_message.text == Config.ERROR_MESSAGE
