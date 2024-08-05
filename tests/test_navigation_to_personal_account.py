from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


def test_personal_account_navigation(driver, go_to_personal_account, log_out):
    # Переход в личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    # Проверка наличия элемента на странице личного кабинета
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
