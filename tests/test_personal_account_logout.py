from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import Config
from locators import Locators


def test_personal_account_logout(driver, go_to_personal_account):
    # Переход в личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    (WebDriverWait(driver, 5)
     .until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON)))

    # Выход из аккаунта
    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Config.LOGIN_URL))

    assert driver.current_url == Config.LOGIN_URL
