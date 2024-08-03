import pytest
import random
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.NAME, 'name').send_keys(email)
        driver.find_element(By.NAME, 'Пароль').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, '.button_button__33qZ0').click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
    return _login_user


@pytest.fixture
def go_to_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.CSS_SELECTOR, '.button_button__33qZ0').click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    driver.find_element(By.NAME, 'name').send_keys('lisasolominskaia12666@yandex.ru')
    driver.find_element(By.NAME, 'Пароль').send_keys('123456')
    driver.find_element(By.CSS_SELECTOR, '.button_button__33qZ0').click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
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
def navigate_to_login(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.CSS_SELECTOR, '.button_button__33qZ0').click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))


@pytest.fixture
def log_out(driver):
    yield
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']//p[text()='Личный Кабинет']").click()
    (WebDriverWait(driver, 5)
     .until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Account_button__14Yp3"))).click())
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
