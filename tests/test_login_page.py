from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_via_home_page(driver, login_user, navigate_to_login, log_out):
    login_user('lisasolominskaia12666@yandex.ru', '123456')
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


def test_login_via_personal_account(driver, login_user, log_out):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//nav[@class='AppHeader_header__nav__g5hnF']//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    login_user('lisasolominskaia12666@yandex.ru', '123456')
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


def test_register_and_login(driver, login_user, log_out):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    login_user('lisasolominskaia12666@yandex.ru', '123456')
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


def test_forgot_password_and_login(driver, login_user, log_out):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    login_user('lisasolominskaia12666@yandex.ru', '123456')
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
