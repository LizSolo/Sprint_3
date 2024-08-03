from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_registration(driver, register_user, unique_user):
    name, email = unique_user
    register_user(name, email, '123456')

    # Проверяем перенаправление на страницу входа
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


def test_registration_with_invalid_password(driver, register_user, unique_user):
    name, email = unique_user
    register_user(name, email, '12345')

    # Ожидаем сообщение об ошибке
    error_message = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.input__error'))
    )

    assert error_message.text == 'Некорректный пароль'
