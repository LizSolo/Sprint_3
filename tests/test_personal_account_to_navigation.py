from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import Config
from locators import Locators


def test_navigation_from_personal_account_to_constructor(driver, go_to_personal_account, log_out):
    # Переход в личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))

    # Переход к Конструктору
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    (WebDriverWait(driver, 10)
     .until(expected_conditions.url_to_be(Config.BASE_URL)))


def test_navigation_from_personal_account_to_logo(driver, go_to_personal_account, log_out):
    # Переход в личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))

    # Переход на главную страницу
    driver.find_element(By.CLASS_NAME, 'AppHeader_header__logo__2D0X2').click()
    (WebDriverWait(driver, 10)
     .until(expected_conditions.url_to_be(Config.BASE_URL)))
