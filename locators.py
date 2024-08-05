from selenium.webdriver.common.by import By
from config import Config


class Locators:
    LOGIN_BUTTON = (By.XPATH, f".//button[text()='{Config.LOGIN_BUTTON_TEXT}']")
    EMAIL_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, 'Пароль')
    SUBMIT_BUTTON = (By.XPATH, f".//button[text()='{Config.LOGIN_BUTTON_TEXT}']")
    MAIN_SUBMIT_BUTTON = (By.XPATH, f".//button[text()='{Config.MAIN_LOGIN_BUTTON_TEXT}']")
    ERROR_TEXT = (By.XPATH, f".//p[text()='{Config.ERROR_MESSAGE}']")
    SUBMIT_LINK = (By.XPATH, f".//a[text()='{Config.LOGIN_BUTTON_TEXT}']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, f".//nav[@class='AppHeader_header__nav__g5hnF']//p[text()='{Config.PERSONAL_ACCOUNT_TEXT}']")
    CONSTRUCTOR_BUTTON = (By.XPATH, f".//nav[@class='AppHeader_header__nav__g5hnF']//p[text()='{Config.CONSTRUCTOR_BUTTON_TEXT}']")
    LOGOUT_BUTTON = (By.XPATH, f".//button[text()='{Config.LOGOUT_BUTTON_TEXT}']")
    REGISTER_NAME_INPUT = (By.NAME, 'name')
    REGISTER_EMAIL_INPUT = (By.NAME, 'name')
    REGISTER_PASSWORD_INPUT = (By.NAME, 'Пароль')
