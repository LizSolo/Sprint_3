from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import Config
from locators import Locators


def test_login_via_home_page(driver, login_user, log_out):
    driver.get(Config.BASE_URL)
    driver.find_element(*Locators.MAIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Config.LOGIN_URL))
    login_user(Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD)
    assert driver.current_url == Config.BASE_URL


def test_login_via_personal_account(driver, login_user, log_out):
    driver.get(Config.BASE_URL)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    login_user(Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD)
    assert driver.current_url == Config.BASE_URL
def test_register_and_login(driver, login_user, log_out):
    driver.get(Config.REGISTER_URL)
    driver.find_element(*Locators.SUBMIT_LINK).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Config.LOGIN_URL))
    login_user(Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD)
    assert driver.current_url == Config.BASE_URL

def test_forgot_password_and_login(driver, login_user, log_out):
    driver.get(Config.FORGOT_PASSWORD_URL)
    driver.find_element(*Locators.SUBMIT_LINK).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Config.LOGIN_URL))
    login_user(Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD)
    assert driver.current_url == Config.BASE_URL
