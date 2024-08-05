import pytest
import random
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import Config
from locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def unique_user():
    name = f'Тестимя{random.randint(1, 999)}'
    email = f'testemail{random.randint(1, 999)}@ya.ru'
    return name, email


@pytest.fixture
def login_user(driver):
    def _login_user(email, password):
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Config.BASE_URL))

    return _login_user


@pytest.fixture
def go_to_personal_account(driver):
    driver.get(Config.BASE_URL)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Config.LOGIN_URL))
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Config.TEST_USER_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Config.TEST_USER_PASSWORD)
    driver.find_element(*Locators.SUBMIT_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Config.BASE_URL))
    yield driver


@pytest.fixture
def register_user(driver):
    def _register_user(name, email, password):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        name_elements = driver.find_elements(By.NAME, 'name')
        name_elements[0].send_keys(name)
        name_elements[1].send_keys(email)

        driver.find_element(By.NAME, 'Пароль').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, '.button_button__33qZ0').click()

    return _register_user


@pytest.fixture
def log_out(driver):
    yield
    driver.get(Config.BASE_URL)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    (WebDriverWait(driver, 5)
     .until(expected_conditions.visibility_of_element_located((Locators.LOGOUT_BUTTON))).click())
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Config.LOGIN_URL))
